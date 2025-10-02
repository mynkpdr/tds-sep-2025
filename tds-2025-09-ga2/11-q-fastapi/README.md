# 11. Write a FastAPI server to serve data (1 Marks)

## 1. Problem Description

The objective is to create a web server using FastAPI that can serve data from a provided CSV file. The server must expose an API endpoint that returns a list of students in JSON format. Crucially, this endpoint must support filtering students by their class based on query parameters in the URL.

## 2. Understanding the Requirements

* **Framework**: FastAPI.
* **Data Source**: A CSV file named `q-fastapi.csv` containing `studentId` and `class` columns.
* **API Endpoint**: An endpoint (e.g., `/api`) that returns data in the format `{"students": [...]}`.
* **Filtering**:

  * A request to `/api` with no parameters should return all students.
  * A request like `/api?class=1A` should return only students from class `1A`.
  * A request like `/api?class=1A&class=1B` should return students from both class `1A` and `1B`.
* **Data Order**: The students in the JSON response must be in the same order as they appear in the original CSV file.
* **CORS**: The API must enable Cross-Origin Resource Sharing (CORS) to allow GET requests from any origin.
* **Submission**: The public URL of the deployed and running FastAPI application.

## 3. Step-by-Step Solution

1. **Project Setup**:

   * Create a new project folder (e.g., `fastapi-student-api`).
   * Download the `q-fastapi.csv` file from the exam page and place it in this folder.
   * Create a Python file named `main.py` and a `requirements.txt` file in the same folder.

2. **Write the FastAPI Application (`main.py`)**:

   * The Python script will use FastAPI to create the server and `pandas` to efficiently read and filter the CSV data.
   * The data from `q-fastapi.csv` will be loaded into a DataFrame when the application starts.
   * An endpoint, `/api`, will be defined to handle `GET` requests. It will accept an optional query parameter `class`, which can be specified multiple times.
   * CORS will be enabled using FastAPI's `CORSMiddleware`.

3. **Run the Server Locally for Testing**:

   * Run the server:

     ```bash
     uvicorn main:app --host 0.0.0.0 --port 8000
     ```

   * You can test it by opening your browser or using `curl`:

     * All students: `curl http://127.0.0.1:8000/api`
     * Filtered students: `curl "http://127.0.0.1:8000/api?class=1A&class=2B"`

## 4. Code / Configuration Files

#### `q-fastapi.csv`

*(This file should be downloaded from the exam platform and placed in the project directory.)*

#### `main.py`

```python
import pandas as pd
from typing import List, Optional
from fastapi import FastAPI, Query, Request
from starlette.middleware.cors import CORSMiddleware

# Initialize the FastAPI app
app = FastAPI()

# Enable CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"]
)

@app.middleware("http")
async def add_pna_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Private-Network"] = "true"
    return response

# Load the student data from the CSV file into a pandas DataFrame on startup
try:
    students_df = pd.read_csv("q-fastapi.csv")
except FileNotFoundError:
    # Create a dummy dataframe if the file is not found, to allow the app to start
    students_df = pd.DataFrame(columns=["studentId", "class"])

@app.get("/api")
def get_students(class_filter: Optional[List[str]] = Query(None, alias="class")):
    """
    Serves student data.
    - If no 'class' query parameter is provided, returns all students.
    - If 'class' query parameters are provided, returns students belonging
      to any of the specified classes.
    """
    if not class_filter:
        filtered_df = students_df
    else:
        filtered_df = students_df[students_df["class"].isin(class_filter)]

    return {"students": filtered_df.to_dict("records")}
```

#### `requirements.txt`

```
fastapi
uvicorn
pandas
```

## 5. How to Run and Verify

After running your application locally, submit the API endpoint URL (e.g., `http://127.0.0.1:8000/api`). The automated grader will send `GET` requests to this URL, both with and without `class` query parameters, and validate that the JSON response is correctly formatted, filtered, and ordered.
