# 13. Sum Table Values with Playwright (1 Mark)

## 1. Problem Description

The task is to write a Python script using **Playwright** to automate visiting a series of webpages. Each page contains one or more tables that are generated dynamically by JavaScript. The script must extract all the numerical values from these tables across all pages and calculate their total sum.

This simulates a QA task for "DataDash," a company that needs to validate data in dynamically generated reports.

## 2. Understanding the Requirements

- **Language**: Python.
- **Library**: `playwright`.
- **Input**: A list of URLs (or seeds to generate URLs).
- **Logic**:
  1. Initialize Playwright and launch a browser instance (e.g., Chromium).
  2. Loop through each given URL.
  3. For each URL, navigate to the page and wait for it to load completely.
  4. Find all table cells (`<td>`) on the page.
  5. Iterate through each cell, get its text content, convert it to an integer, and add it to a running total.
  6. After visiting all pages, close the browser.
- **Output**: The final total sum as an integer.

## 3. Step-by-Step Solution

### Step 1: Install Playwright and its Browsers

1. Create a project folder (e.g., `playwright_sum`).
2. Set up and activate a virtual environment.
3. Install the `playwright` library:

   ```bash
   pip install playwright
   ```

4. After installation, you must download the browser binaries that Playwright uses. Run this command:

   ```bash
   playwright install
   ```

   This will download Chromium, Firefox, and WebKit.

5. Create a Python file for your code (e.g., `sum_tables.py`).

### Step 2: Write the Playwright Script

1. **Import**: Import `sync_playwright` from the `playwright.sync_api`.
2. **Define URLs**: Create the list of URLs to visit based on the seeds provided in the question.
3. **Initialize Playwright**: Use a `with sync_playwright() as p:` block to manage the Playwright instance.
4. **Launch Browser**: Launch a browser using `p.chromium.launch(headless=True)`. `headless=True` runs it in the background without opening a UI window, which is faster.
5. **Loop and Scrape**:
   - Create a new page context for each URL.
   - Use `page.goto(url)` to navigate.
   - Use `page.locator("td")` to get all table cell elements. This is a modern Playwright feature that waits automatically for elements to appear.
   - Iterate through the locators, get their `inner_text()`, convert to `int`, and add to a `total_sum` variable.
6. **Close Browser**: Ensure `browser.close()` is called at the end.
7. **Print Result**: Print the final sum.

## 4. Code (`sum_tables.py`)

```python
from playwright.sync_api import sync_playwright

def sum_js_tables(base_url: str, seeds: list[str]) -> int:
    """
    Uses Playwright to visit multiple pages, finds all numbers in tables,
    and returns their sum.

    Args:
        base_url (str): The base URL for the pages.
        seeds (list[str]): A list of seeds to generate the full URLs.

    Returns:
        int: The total sum of all numbers found in the tables.
    """
    total_sum = 0

    with sync_playwright() as p:
        # Launch a headless browser (headless=True means no UI is shown)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for seed in seeds:
            url = f"{base_url}?seed={seed}"
            print(f"Navigating to {url}...")

            try:
                page.goto(url, wait_until="domcontentloaded")

                # Use a locator to find all table cells (td)
                # Playwright's locators auto-wait, which is robust
                cells = page.locator("td")

                # Get the count for logging
                cell_count = cells.count()
                print(f"  Found {cell_count} cells.")

                # Iterate through each cell and add its value to the sum
                for i in range(cell_count):
                    cell_text = cells.nth(i).inner_text()
                    if cell_text.isdigit():
                        total_sum += int(cell_text)

            except Exception as e:
                print(f"  An error occurred on page {url}: {e}")
                continue # Move to the next seed

        # Close the browser instance
        browser.close()

    return total_sum


if __name__ == "__main__":
    # --- Replace these with the values from your question ---
    # The problem specifies a range of seeds to use.
    # For example, if the start seed is 76 and the end seed is 85:
    start_seed = 76
    end_seed = 85
    SEEDS_TO_PROCESS = [str(i) for i in range(start_seed, end_seed + 1)]
    BASE_URL = "https://sanand0.github.io/tdsdata/js_table/"
    # ---------------------------------------------------------

    print(f"Processing seeds: {SEEDS_TO_PROCESS}")
    final_sum = sum_js_tables(BASE_URL, SEEDS_TO_PROCESS)

    print("\n--- Result ---")
    print(f"The total sum of all numbers in the tables is: {final_sum}")
    print("----------------\n")
```

## 5. How to Run

1. Ensure you have installed `playwright` and run `playwright install`.
2. Save the code as `sum_tables.py`.
3. Modify the `start_seed` and `end_seed` variables at the bottom of the script to match the range specified in your question.
4. Run the script from your terminal:

   ```bash
   python sum_tables.py
   ```

5. The script will launch a headless browser, visit each page, and print its progress. Finally, it will output the total sum, which is your answer.
