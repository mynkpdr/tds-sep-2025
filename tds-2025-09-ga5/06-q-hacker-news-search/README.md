# 6. Search Hacker News (0.5 Marks)

## 1. Problem Description

The task is to write a Python script that searches the Hacker News RSS feed for the most recent post that matches a specific topic (e.g., "Python") and has at least a certain number of points (upvotes). The script should then extract and return the URL of that post.

This simulates a task for "TechInsight Analytics," a market research firm that monitors tech trends by analyzing popular online discussions.

## 2. Understanding the Requirements

- **Language**: Python.
- **Libraries**: `requests` and Python's built-in `xml.etree.ElementTree`.
- **API**: HNRSS (`https://hnrss.org/`), which provides custom RSS feeds for Hacker News.
- **Input**: A search query (topic) and a minimum number of points.
- **Logic**:
  1. Construct the URL for the HNRSS API. The URL format allows for querying by topic and minimum points (e.g., `https://hnrss.org/newest?q=Python&points=100`).
  2. Fetch the content from this URL, which will be in XML format.
  3. Parse the XML to find the first `<item>` element, which represents the newest matching post.
  4. Within that item, find the `<link>` tag and extract its text content.
- **Output**: The URL string of the found post.

## 3. Step-by-Step Solution

### Step 1: Set Up Environment

1. Create a project folder (e.g., `hn_search`).
2. Set up a virtual environment and activate it.
3. Install the `requests` library: `pip install requests`.
4. Create a Python file (e.g., `search_hn.py`).

### Step 2: Write the Python Script

1. **Import Libraries**: Import `requests` and `xml.etree.ElementTree`.
2. **Define Inputs**: Store the search query and minimum points in variables.
3. **Construct URL**: Build the HNRSS URL with the query and points as parameters.
4. **Fetch and Parse XML**:
   - Use `requests.get()` to fetch the RSS feed.
   - Use `ElementTree.fromstring()` to parse the XML content from the response text.
   - The XML structure contains a `<channel>` which contains multiple `<item>`s. We need the first one.
5. **Extract Link**: Use `find('./channel/item/link')` to navigate the XML tree and get the link element. If found, extract its `.text` property.
6. **Handle Errors**: If no item is found, the script should report that, as the search might yield no results.
7. **Print Result**: Print the extracted URL.

## 4. Code (`search_hn.py`)

```python
import requests
import xml.etree.ElementTree as ET

def find_latest_hn_post(query: str, min_points: int) -> str:
    """
    Searches HNRSS for the latest post matching a query and minimum points.

    Args:
        query (str): The search term (e.g., "Python").
        min_points (int): The minimum number of points the post must have.

    Returns:
        str: The URL of the first matching post.
    """
    hnrss_url = "https://hnrss.org/newest"
    params = {
        "q": query,
        "points": min_points
    }

    print(f"Searching for '{query}' with at least {min_points} points...")

    try:
        response = requests.get(hnrss_url, params=params)
        response.raise_for_status()

        # The response is XML, so we parse it directly
        root = ET.fromstring(response.content)

        # The link is inside the first <item> tag within the <channel>
        # XPath to find the link: ./channel/item/link
        link_element = root.find('./channel/item/link')

        if link_element is not None and link_element.text:
            return link_element.text.strip()
        else:
            raise ValueError("No matching post found in the RSS feed.")

    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to fetch data from HNRSS: {e}")


if __name__ == "__main__":
    # --- Replace these with the values from your question ---
    SEARCH_QUERY = "Python"
    MINIMUM_POINTS = 100
    # ---------------------------------------------------------

    try:
        post_url = find_latest_hn_post(SEARCH_QUERY, MINIMUM_POINTS)
        print("\n--- Result ---")
        print(f"Found URL: {post_url}")
        print("----------------\n")
    except (ValueError, ConnectionError) as e:
        print(f"An error occurred: {e}")
```

## 5. How to Run

1. Save the code as `search_hn.py`.
2. Modify the `SEARCH_QUERY` and `MINIMUM_POINTS` variables to match your specific question.
3. Run the script from your terminal:

   ```bash
   python search_hn.py
   ```

4. The script will print the URL of the newest matching post. This URL is your answer.
