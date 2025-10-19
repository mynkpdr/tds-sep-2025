# 8. Vector Databases (1 Mark)

## 1. Problem Description

The task is to build a simple web service (an API) that performs "semantic search." The API will receive a list of documents and a search query. It should then find the three documents that are most semantically similar to the query and return them in order of relevance. This is a core component of modern search systems and RAG (Retrieval Augmented Generation) applications.

## 2. Understanding the Requirements

- **Framework**: The API should be built using a Python web framework like **FastAPI**.
- **Endpoint**: It must have a `POST` endpoint at a path like `/similarity`.
- **Request Format**: The endpoint must accept a JSON body with two keys:
  - `"docs"`: A list of strings, where each string is a document.
  - `"query"`: A single string representing the search query.
- **Embedding Model**: All text (documents and query) must be converted to embedding vectors using OpenAI's `text-embedding-3-small` model.
- **Similarity Calculation**: The relevance of documents should be determined by calculating the cosine similarity between the query's embedding and each document's embedding.
- **Response Format**: The API should return a JSON object with a single key `"matches"`, whose value is a list of the top 3 most similar document strings, sorted from most to least similar.
- **CORS**: The API must have CORS (Cross-Origin Resource Sharing) enabled to allow requests from any website.

## 3. Step-by-Step Solution

### Step 1: Set up the Project

1. Create a new project folder.
2. Install the necessary libraries: `fastapi`, `uvicorn`, `pydantic`, `openai`, and `scikit-learn` (for easy similarity calculation).

   ```bash
   pip install "fastapi[all]" openai scikit-learn
   ```

3. Replace your OpenAI API key.
   - You can set it as an environment variable `OPENAI_API_KEY` or directly in the code (not recommended for production).

### Step 2: Write the FastAPI Code

Create a Python file (e.g., `main.py`).

1. **Imports**: Import necessary components from `fastapi`, `pydantic`, `openai`, etc.
2. **OpenAI Client**: Initialize the OpenAI client.
3. **Data Models**: Use Pydantic to define models for the request body (`SearchRequest`) and response.
4. **FastAPI App**: Create a FastAPI app instance and enable CORS.
5. **Endpoint Logic**:
   - Define the `/similarity` `POST` endpoint.
   - Inside the function, combine the query and all documents into a single list of texts.
   - Make **one** API call to OpenAI's embedding endpoint to get embeddings for all texts at once. This is much more efficient.
   - Separate the query embedding from the document embeddings.
   - Use `sklearn.metrics.pairwise.cosine_similarity` to calculate the similarity between the query vector and all document vectors.
   - Pair each document with its similarity score.
   - Sort the pairs in descending order based on the score.
   - Extract the text from the top 3 pairs.
   - Return the result in the required format.

### Step 3: Run the API

1. Run the application from your terminal using Uvicorn:

   ```bash
   uvicorn main:app --reload --port 8000
   ```

2. Your API will be running at `http://127.0.0.1:8000` and publicly accessible for the exam using Private Network Access.

### Step 4: Submit the URL

Once your API is running and accessible, submit that URL as your answer. For example: `http://127.0.0.1:8000/similarity`.

## 4. Code / Configuration File

Here is the complete `main.py` file for the FastAPI application.

```python
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Initialize OpenAI client (Change the API key as needed)
client = OpenAI(base_url="https://aipipe.org/openai/v1", api_key="AIPIPE_API_KEY")

# --- Pydantic Models for Request and Response ---
class SearchRequest(BaseModel):
    docs: list[str]
    query: str

class SearchResponse(BaseModel):
    matches: list[str]

# --- FastAPI App Initialization ---
app = FastAPI()

# Enable CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Add Private Network header
@app.middleware("http")
async def add_pna_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Private-Network"] = "true"
    return response

# --- API Endpoint ---
@app.post("/similarity", response_model=SearchResponse)
def find_similar_documents(request: SearchRequest):
    # Combine query and docs to get all embeddings in one API call
    all_texts = [request.query] + request.docs

    # Get embeddings from OpenAI
    response = client.embeddings.create(
        input=all_texts,
        model="text-embedding-3-small"
    )

    # Extract embedding vectors
    embeddings = [item.embedding for item in response.data]

    # Separate query embedding from doc embeddings
    query_embedding = np.array(embeddings[0]).reshape(1, -1)
    doc_embeddings = np.array(embeddings[1:])

    # Calculate cosine similarity
    similarities = cosine_similarity(query_embedding, doc_embeddings).flatten()

    # Pair documents with their similarity scores
    doc_similarity_pairs = list(zip(request.docs, similarities))

    # Sort by similarity in descending order
    sorted_docs = sorted(doc_similarity_pairs, key=lambda item: item[1], reverse=True)

    # Get the top 3 matching document texts
    top_3_matches = [doc for doc, score in sorted_docs[:3]]

    return {"matches": top_3_matches}

```

## 5. How to Verify

The exam platform will send a `POST` request to the URL you provide. The request will contain a JSON body with a test `docs` array and `query` string. The platform will then check if your API:

- Responds successfully (with a 200 status code).
- Returns a valid JSON object.
- The JSON contains a `"matches"` key with a list of 3 strings.
- The 3 strings are the correct documents, sorted by relevance.
