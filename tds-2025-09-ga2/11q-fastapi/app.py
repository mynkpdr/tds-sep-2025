# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "fastapi",
#   "uvicorn"
# ]
# ///

from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import csv
from typing import List, Optional

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # Allows all origins
    allow_methods=["*"],
    allow_headers=["*"]
    # expose_headers=["*"]    # Expose all the headers to the browser in response
)

# Load students data from CSV once at startup
STUDENTS = []
CSV_FILE = "q-fastapi.csv"  # Replace with your CSV file path

with open(CSV_FILE, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        STUDENTS.append({
            "studentId": int(row["studentId"]),
            "class": row["class"]
        })


@app.get("/api")
def get_students(class_: Optional[List[str]] = Query(None, alias="class")):
    if class_:
        # Filter students by class
        filtered = [s for s in STUDENTS if s["class"] in class_]
        return JSONResponse(content={"students": filtered})
    else:
        return JSONResponse(content={"students": STUDENTS})

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8003, reload=True)