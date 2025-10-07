# 7. FastAPI + CLI Coding Agent (2 Marks)

## 1. Problem Description

The task is to build and deploy a public web service using Python's FastAPI framework. This service must expose a `GET` endpoint at `/task` that accepts a query parameter `q`. The endpoint will pass the value of `q` as a prompt to a command-line (CLI) coding agent (here, **GitHub Copilot CLI**), execute it, and return the agent's output in a structured JSON format.

## 2. Understanding the Requirements

* **Framework**: FastAPI (Python).
* **Endpoint**: A public `GET /task` route.
* **Input**: A URL query parameter `q` containing the task description (e.g., `.../task?q=write a script to...`).
* **Logic**:

  1. The FastAPI application receives the request.
  2. It executes **Copilot CLI** in a subprocess, using `q` as the prompt.
  3. It captures the standard output from the CLI agent.
* **Output**: A JSON response with the following structure:

    ```json
    {
    "task": "The original task from q",
    "agent": "copilot-cli",
    "output": "The captured output from the agent",
    "email": "23f3004197@ds.study.iitm.ac.in"
    }
    ```

* **Deployment**: The final endpoint will run **locally only**.

## 3. Step-by-Step Solution

### Step 1: Set Up Your Local Python Environment

1. Make sure you have Python installed.
2. Create a project folder (e.g., `fastapi-agent`) and navigate into it.
3. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

4. Install the necessary libraries:

```bash
pip install fastapi "uvicorn[standard]"
```

5. Install **Copilot CLI** globally:

```bash
npm install -g @github/copilot
```

6. Run Copilot CLI and log in:

```bash
copilot
```

Follow the instructions to authenticate, then exit.

---

### Step 2: Write the FastAPI Application

Create a file named `main.py` with the following code:

```python
import subprocess
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI app
app = FastAPI()

# Configure CORS to allow cross-origin requests
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

@app.get("/task")
def run_cli_agent(q: str):
    """
    This endpoint takes a query 'q', passes it to Copilot CLI,
    and returns the agent's output.
    """
    agent_name = "copilot-cli"
    command = ["copilot", "--allow-all-tools", "-p", q]

    try:
        # Execute the command and capture the output
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
            timeout=120
        )
        agent_output = result.stdout.strip()
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        agent_output = f"Error executing agent: {e}"

    # Structure the response
    response_data = {
        "task": q,
        "agent": agent_name,
        "output": agent_output,
        "email": "23f3004197@ds.study.iitm.ac.in",
    }

    return response_data

@app.get("/")
def read_root():
    return {"message": "CLI Agent API is running locally. Use the /task endpoint."}
```

---

### Step 3: Run the Server Locally

```bash
uvicorn main:app --reload
```

Test it in your browser:

```bash
http://127.0.0.1:8000/task?q=Hello+world
```

You should see a JSON response with Copilot’s output. If you encounter issues, ensure Copilot CLI is correctly **installed** and **authenticated**.

---

### Step 4: Verify the Local Endpoint

1. Use your local server to test:

```bash
http://127.0.0.1:8000/task?q=Write+a+Python+script+that+prints+the+12th+Fibonacci+number
```

2. You should see a JSON response like:

```json
{
  "task": "Write a Python script that prints the 12th Fibonacci number",
  "agent": "copilot-cli",
  "output": "...Copilot output...",
  "email": "23f3004197@ds.study.iitm.ac.in"
}
```
