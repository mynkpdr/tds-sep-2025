import pandas as pd
from typing import List, Optional
from fastapi import FastAPI, Query, Request
from starlette.middleware.cors import CORSMiddleware

# Initialize the FastAPI app
app = FastAPI()

# Enable CORS to allow requests from any origin
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["GET"])


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
