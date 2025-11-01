# 2. Scrape IMDb movies (1 Marks)

## 1. Problem Description

The task is to build a Python script that scrapes movie data from IMDb's advanced search page. The script should filter movies by a specific user rating range (e.g., between 4.0 and 8.0), extract key details for the first 50 results, and format them into a JSON structure.

This project simulates a content acquisition task for a streaming service, "StreamFlix," which needs to identify high-quality movies to add to its library.

## 2. Understanding the Requirements

- **Language**: Python.
- **Libraries**: `requests` (to fetch the webpage), `lxml` or `beautifulsoup4` (to parse HTML), and `json` (to format the output).
- **Data Source**: IMDb advanced title search (`https://www.imdb.com/search/title/`).
- **Input**: A minimum and maximum user rating.
- **Logic**:
  1. Construct the correct URL to filter movies by the given rating range.
  2. Fetch the HTML content of the search results page.
  3. Parse the HTML to find the list of movie items.
  4. For each movie, extract its ID, title, release year, and rating.
  5. Collect the data into a list of dictionaries.
- **Output**: A JSON string representing the list of extracted movie data.

## 3. Step-by-Step Solution

### Step 1: Set Up Your Python Environment

1. Create a project folder (e.g., `imdb_scraper`).
2. It's good practice to create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the necessary libraries:

   ```bash
   pip install requests beautifulsoup4
   ```

4. Create a Python file for your code (e.g., `main.py`).

### Step 2: Write the Scraping Logic

1. **Construct URL**: The URL for searching by user rating looks like this: `https://www.imdb.com/search/title/?user_rating=4.0,8.0`. The script will dynamically insert the min and max ratings.
2. **Send Request**: Use `requests.get()` to fetch the page. It's crucial to include a `User-Agent` header to mimic a real browser and avoid being blocked. An `Accept-Language` header helps get results in English.
3. **Parse HTML**: Use `BeautifulSoup` to parse the response text. The movie data is contained within list items with a specific CSS class (`.ipc-metadata-list-summary-item`).
4. **Extract Data**: Loop through each movie item and use CSS selectors to find the elements containing the title, year, rating, and ID.
   - **Title**: Found in an `h3` tag.
   - **Year & Metadata**: Found in a `div` with class `.dli-title-metadata-item`.
   - **Rating**: Found in a `span` with class `.ipc-rating-star`.
   - **ID**: Extracted from the `href` attribute of the title's link.
5. **Format Output**: Store the extracted data in a list of dictionaries and use the `json` library to print it in the required format.

## 4. Code (`main.py`)

```python
import requests
import json
from bs4 import BeautifulSoup
import re

def scrape_imdb_movies(min_rating, max_rating):
    """
    Scrapes IMDb for movies within a specified rating range.
    Returns a JSON string containing the movie data.
    """
    # Construct URL with rating filter
    url = f"https://www.imdb.com/search/title/?user_rating={min_rating},{max_rating}"

    # Request headers to mimic a browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }

    # Fetch the page
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    movie_list = []

    # Select all movie items
    list_items = soup.select(".ipc-metadata-list-summary-item")

    for item in list_items:
        try:
            # Extract title
            title_wrapper = item.select_one(".ipc-title-link-wrapper")
            if not title_wrapper:
                continue
            title = title_wrapper.select_one("h3.ipc-title__text").text

            # Extract IMDb ID
            href = title_wrapper.get('href', '')
            movie_id_match = re.search(r'/title/(tt\d+)/', href)
            movie_id = movie_id_match.group(1) if movie_id_match else None

            # Extract year
            metadata_items = item.select(".dli-title-metadata-item")
            year = metadata_items[0].text if metadata_items else None

            # Extract rating
            rating_element = item.select_one(".ipc-rating-star")
            rating = rating_element.text.strip().split()[0] if rating_element else None

            # Add to list if all fields exist
            if all([movie_id, title, year, rating]):
                movie_list.append({
                    "id": movie_id,
                    "title": title,
                    "year": year,
                    "rating": rating
                })
        except (AttributeError, IndexError):
            continue  # Skip item if parsing fails

    # Return JSON with proper Unicode characters
    return json.dumps(movie_list, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    # Example usage
    MIN_RATING = 4.0
    MAX_RATING = 8.0

    json_output = scrape_imdb_movies(MIN_RATING, MAX_RATING)
    print(json_output)
```

## 5. How to Run

1. Make sure you have installed `requests` and `beautifulsoup4`.
2. Save the code above as `main.py`.
3. Open your terminal, navigate to the project folder, and run the script:

   ```bash
   python main.py
   ```

4. The script will print the scraped data as a JSON string to the console. You can copy this output and submit it as your answer.
