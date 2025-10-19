# 9. RAG: TypeScript Book (1 Mark)

## 1. Problem Description

The goal is to build a Retrieval Augmented Generation (RAG) system as a web API. This API will answer questions about the TypeScript programming language by using Simon Willson's `llm` CLI to find relevant information in the "TypeScript Book" documentation and generate an answer based _only_ on that information. This approach ensures answers are accurate and grounded in a specific knowledge base, all orchestrated through command-line tools wrapped in a simple API.

## 2. Understanding the Requirements

- **Framework**: The API can be built with any Python web framework (e.g., **FastAPI**).
- **Endpoint**: It must have a `GET` endpoint, for example, `/search`, that accepts a query parameter `q`. The full request would look like `/search?q=Your question here`.
- **Knowledge Base**: The system must use the content from the [TypeScript Book GitHub repository](https://github.com/basarat/typescript-book/).
- **RAG Pipeline**: The backend must wrap the `llm` CLI tool to perform a full RAG process:
  1. **Retrieve**: Use `llm similar` to find the most relevant text chunks from the indexed TypeScript Book based on the user's question.
  2. **Augment**: Pipe the retrieved text chunks (as context) along with the original question into a new prompt for a generative AI model.
  3. **Generate**: Use `llm -s` to get the final answer from the AI model.
- **Response Format**: The API must return a JSON object containing at least an `"answer"` key with the AI-generated answer and a `"sources"` key with the IDs of the retrieved chunks.
- **CORS**: The API must have CORS enabled to be testable from the browser.

## 3. Step-by-Step Solution

This is a two-part process: an offline data preparation step performed on the command line, and an online API implementation step to wrap the CLI commands.

### Part 1: Offline Data Preparation (Indexing the Book via CLI)

This only needs to be done once before you start the API. This process uses the command line directly as described in the `llm` CLI RAG tutorial.

1. **Get the Data**: Clone the TypeScript Book repository.

   ```bash
   git clone --depth 1 https://github.com/basarat/typescript-book
   cd typescript-book
   ```

2. **Process and Chunk the Data**: Run the following shell command to find all Markdown files, split them into chunks, and format them as newline-delimited JSON (`chunks.json`). It may take a few minutes to run.

   ```bash
   (
     shopt -s globstar
     for f in **/*.md; do
       uvx --from split_markdown4gpt mdsplit4gpt "$f" --model gpt-4o --limit 4096 --separator "===SPLIT===" \
       | sed '1s/^/===SPLIT===\n/' \
       | jq -R -s -c --arg file "$f" '
         split("===SPLIT===")[1:]
         | to_entries
         | map({
             id: ($file + "#" + (.key | tostring)),
             content: .value
           })[]
       '
     done
   ) | tee chunks.json
   ```

3. **Create and Store Embeddings**: Use `llm embed-multi` to process `chunks.json`, generate an embedding for each chunk using OpenAI's model, and store them in a local collection named `typescript-book`.

   ```bash
   # Ensure you have already setup the llm CLI tool.
   llm embed-multi typescript-book --model 3-small --store --format nl chunks.json
   ```

   This command creates a searchable vector index managed by `llm` in its default local database.

### Part 2: Online API Implementation (Wrapping the CLI)

1. **Set up FastAPI Project**: Install the necessary libraries.

   ```bash
   pip install fastapi uvicorn
   ```

2. **Write the API Code (`main.py`)**: Create a Python script that uses the `subprocess` module to call the `llm` commands you used manually. The API will execute these commands and format their output as JSON.
3. **Run and Submit**: Run your API using `uvicorn main:app --reload --port 8001`. Submit the URL of your `/search` endpoint.

## 4. Code / Configuration File

This `main.py` file implements the FastAPI server. It acts as a web interface for the `llm` commands, effectively turning your command-line RAG process into an API.

```python
import subprocess
import json
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware

# --- FASTAPI APP ---
app = FastAPI(
    title="RAG API with LLM CLI",
    description="An API that uses Simon Willson's llm CLI for RAG.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add Private Network header
@app.middleware("http")
async def add_pna_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Private-Network"] = "true"
    return response

# --- RAG PROMPT TEMPLATE ---
RAG_PROMPT_TEMPLATE = "Based only on the context provided, answer the following question: {question}"

# --- API ENDPOINT ---
@app.get("/search")
def search_and_answer(q: str):
    """
    Performs a RAG lookup using the llm CLI.
    1. Finds similar documents using 'llm similar'.
    2. Generates an answer based on those documents using 'llm -s'.
    """
    if not q:
        raise HTTPException(status_code=400, detail="Query parameter 'q' is missing.")

    # --- 1. RETRIEVE Step ---
    try:
        retrieve_command = [
            "llm", "similar", "typescript-book",
            "-n", "3",
            "-c", q
        ]

        similar_result = subprocess.run(
            retrieve_command,
            check=True,
            capture_output=True,
            text=True
        )

        output_lines = similar_result.stdout.strip().split('\n')
        retrieved_docs = [json.loads(line) for line in output_lines if line]

    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="The 'llm' command was not found. Is it installed and in your PATH?")
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving documents: {e.stderr}")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Failed to parse JSON from 'llm similar'.")

    if not retrieved_docs:
        return {"answer": "Could not find relevant documents in the TypeScript Book.", "sources": []}

    # Extract context and sources from the retrieved documents
    context = "\n\n---\n\n".join([doc['content'] for doc in retrieved_docs])
    sources = [doc['id'] for doc in retrieved_docs]

    # --- 2. AUGMENT & 3. GENERATE Step ---
    try:
        prompt = RAG_PROMPT_TEMPLATE.format(question=q)
        generate_command = ["llm", "-m", "gpt-5", "-s", prompt]

        generate_result = subprocess.run(
            generate_command,
            input=context,
            capture_output=True,
            text=True,
            check=True
        )
        answer = generate_result.stdout.strip()
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Error generating answer: {e.stderr}")

    return {"answer": answer, "sources": sources}
```

## 5. How to Verify

The platform will send `GET` requests to your submitted URL with different questions about TypeScript (e.g., `.../search?q=What is a property initializer?`). It will then check the `answer` in your JSON response to see if it contains the correct information, which should be grounded in the TypeScript Book documentation retrieved by the `llm` CLI.
