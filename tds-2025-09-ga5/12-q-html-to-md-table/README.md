# 12. Convert HTML Table to Markdown (1 Mark)

## 1. Problem Description

The task is to write a script that fetches a specific webpage, finds the HTML table on it, and converts that table into Markdown table format.

This simulates a task for "TableNinja," a service that aggregates HTML reports and converts them to Markdown for easier version control and review.

## 2. Understanding the Requirements

- **Language**: Python.
- **Libraries**: `requests`, `beautifulsoup4`, and a helper library like `markdownify` is useful.
- **Input**: A URL pointing to a page containing an HTML table.
- **Logic**:
  1. Fetch the HTML content from the URL.
  2. Parse the HTML and find the `<table>` element.
  3. Convert the `<table>` element and its contents (`<thead>`, `<tbody>`, `<tr>`, `<th>`, `<td>`) into a Markdown table string.

- **Output**: A string containing the Markdown table.

---

## Method 1: Using Python Script

### Step 1: Set Up Environment

1. Create a project folder (e.g., `html_to_markdown`).

2. Set up and activate a virtual environment.

3. Install the required libraries. `markdownify` is excellent for this conversion.

   ```bash
   pip install requests beautifulsoup4 markdownify
   ```

4. Create a Python file (e.g., `convert_table.py`).

### Step 2: Write the Python Script

1. **Import Libraries**: `requests`, `BeautifulSoup`, and `markdownify`.
2. **Define Function**: Create a function `convert_html_table_to_md` that takes the URL as an argument.
3. **Fetch and Parse**: Use `requests.get()` to fetch the page and `BeautifulSoup` to parse it.
4. **Find Table**: Use `soup.find('table')` to locate the table element. If there are multiple tables, you might need a more specific selector.
5. **Convert to Markdown**: The `markdownify` library makes this easy. Pass the string representation of the table element to the `markdownify()` function. It will handle the conversion automatically.
6. **Return Markdown**: The function returns the resulting Markdown string.
7. **Main Block**: Call the function with the URL from your problem and print the result.

### Step 3: Code (`convert_table.py`)

```python
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

def convert_html_table_to_md(url: str) -> str:
    """
    Fetches a webpage, finds the first HTML table, and converts it to Markdown.

    Args:
        url (str): The URL of the webpage containing the table.

    Returns:
        str: The Markdown representation of the table.
    """
    print(f"Fetching table from {url}...")

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Could not fetch the URL: {e}")

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the first table on the page
    table = soup.find('table')

    if not table:
        raise ValueError("No <table> element found on the page.")

    # Convert the table HTML to Markdown
    markdown_table = md(str(table))

    return markdown_table

if __name__ == "__main__":
    report_id = 38  # Replace with the number from your specific question
    TARGET_URL = f"https://sanand0.github.io/tdsdata/html_table/{report_id}.html"

    try:
        md_table = convert_html_table_to_md(TARGET_URL)
        print("\n--- Markdown Table ---")
        print(md_table)
        print("----------------------\n")
    except (ConnectionError, ValueError) as e:
        print(f"An error occurred: {e}")
```

### Step 4: How to Run

1. Save the code as `convert_table.py`.

2. Update the `report_id` variable at the bottom of the script to match the number in the URL from your question.

3. Run the script from your terminal:

   ```bash
   python convert_table.py
   ```

4. The script will print the Markdown table to the console. Copy this output and paste in the answer box.

---

## Method 2: Using an Online Converter

Instead of writing Python code, you can use an online tool like [HTML to Markdown](https://htmlmarkdown.com/) to convert your table:

### Steps

1. Open the URL in your browser and **view the page source** (Right-click → “View Page Source”).
2. Copy the HTML code for the table (everything between `<table>` and `</table>`).
3. Go to [https://htmlmarkdown.com/](https://htmlmarkdown.com/).
4. Paste the HTML table code into the **input box**.
5. Click **Convert HTML to Markdown**.
6. The Markdown version of the table will appear in the output box.
7. Copy the Markdown and paste in the answer box.
