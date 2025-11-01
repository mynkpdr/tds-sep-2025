# 3. Wikipedia Outline (0.5 Marks)

## 1. Problem Description

The task is to build a web API that takes a country name as input, fetches its corresponding English Wikipedia page, extracts all the headings (H1 to H6), and returns them as a structured Markdown outline.

This project simulates a service for an educational platform, "GlobalEdu," which needs to display structured, easy-to-navigate summaries of countries for its students.

## 2. Understanding the Requirements

- **Framework**: A Python web framework like **FastAPI**.
- **Endpoint**: A `GET` endpoint (e.g., `/outline`) that accepts a query parameter `country`.
- **Input**: A country name string (e.g., `/outline?country=Switzerland`).
- **Logic**:
  1. Receive the country name from the query parameter.
  2. Construct the Wikipedia URL for that country (e.g., `https://en.wikipedia.org/wiki/Switzerland`).
  3. Fetch the HTML content of the page.
  4. Parse the HTML to find all heading tags (`<h1>` to `<h6>`).
  5. For each heading, generate a Markdown line (e.g., `<h2>History</h2>` becomes `## History`).
  6. Combine these lines into a single string.
- **Output**: The API should return the Markdown outline as a plain text response.
- **CORS**: The API must have Cross-Origin Resource Sharing (CORS) enabled to allow requests from any origin.

## 3. Step-by-Step Solution

### Step 1: Set up the FastAPI Project

1. Create a project folder (e.g., `wiki_api`).
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the necessary libraries: FastAPI, Uvicorn (the server), requests, and BeautifulSoup.

   ```bash
   pip install "fastapi[all]" requests beautifulsoup4
   ```

4. Create a Python file for your code (e.g., `main.py`).

### Step 2: Write the API Logic in `main.py`

1. **Import Libraries**: Import `FastAPI`, `Request`, `CORSMiddleware`, `requests`, `BeautifulSoup`, and `Response` for returning plain text.
2. **Initialize App**: Create a `FastAPI` app instance and add `CORSMiddleware` to handle CORS.
3. **Create Endpoint**: Define an `async def` function for the `/outline` endpoint.
4. **Fetch and Parse**: Inside the function, construct the Wikipedia URL. Use `requests` to get the page content. Use `BeautifulSoup` to parse it and find all heading tags (`h1`, `h2`, `h3`, `h4`, `h5`, `h6`).
5. **Generate Markdown**: Iterate through the found headings. For each heading tag, determine its level (e.g., `h2` is level 2) and create a Markdown string with the corresponding number of `#` characters followed by the heading's text.
6. **Return Response**: Join all the Markdown lines with newlines and return them as a `Response` with `media_type="text/plain"`.

## 4. Code (`main.py`)

```python
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response

# --- FastAPI App Initialization ---
app = FastAPI(
    title="Wikipedia Outline API",
    description="An API to fetch a Markdown outline of a country's Wikipedia page.",
    version="1.0.0",
)

# Enable CORS to allow requests from any origin
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

@app.get("/outline", response_class=Response)
async def get_wikipedia_outline(country: str = Query(..., description="The name of the country to look up.")):
    """
    Fetches the Wikipedia page for a given country, extracts its headings,
    and returns them as a Markdown-formatted outline.
    """
    # Sanitize and format country name for URL (e.g., "South Korea" -> "South_Korea")
    formatted_country = country.strip().replace(" ", "_")
    url = f"https://en.wikipedia.org/wiki/{formatted_country}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        # Raise an exception if the page doesn't exist (e.g., 404 Not Found)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=404, detail=f"Could not find a Wikipedia page for '{country}'. Error: {e}")

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all heading tags from h1 to h6
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    markdown_outline = []
    for heading in headings:
        # Get the heading level from the tag name (e.g., 'h2' -> 2)
        level = int(heading.name[1])
        # Get the clean text, removing any nested tags like '[edit]'
        text = heading.get_text(strip=True).replace('[edit]', '')

        # Create the Markdown heading
        if text: # Only add if there is text
             markdown_outline.append(f"{'#' * level} {text}")

    if not markdown_outline:
        raise HTTPException(status_code=404, detail=f"No headings found on the Wikipedia page for '{country}'.")

    # Join all lines into a single string and return as plain text
    full_outline = "\n".join(markdown_outline)
    return Response(content=full_outline, media_type="text/plain")

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Wikipedia Outline API!",
        "usage": "Navigate to /docs for the interactive API documentation."
    }

```

## 5. How to Run and Verify

1. Ensure you have all the required packages installed.
2. Save the code as `main.py`.
3. Run the Uvicorn server from your terminal:

   ```bash
   uvicorn main:app --reload --port 8000
   ```

4. The API will be running locally. To verify, open your web browser and go to one of the following URLs:
   - `http://127.0.0.1:8000/outline?country=Germany`
   - `http://127.0.0.1:8000/outline?country=Switzerland`
5. You should see the Markdown outline displayed in your browser. The URL of your running endpoint (e.g., `http://127.0.0.1:8000/outline`) is what you would submit.
