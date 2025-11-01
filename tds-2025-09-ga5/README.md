# Summary of all the questions

### **Question 1: Import HTML to Google Sheets**

- **What it Covered:** Analyzing cricket batting statistics from ESPN Cricinfo. The task involved using **Google Sheets** and its built-in `=IMPORTHTML()` function to import a specific data table from the website and then using the `=SUM()` function to calculate the total number of "ducks" (scores of "0") listed on that page.
- **Why you need it:** This simulates a real-world task for a sports analytics firm. It demonstrates how to efficiently gather and analyze player performance data directly from live web sources using common spreadsheet tools, without needing to write any code.

### **Question 2: Scrape IMDb movies**

- **What it Covered:** Writing a **Python** script using the `requests` and `beautifulsoup4` libraries to scrape the IMDb advanced title search page. The script constructs a URL to filter movies by a specific user rating range, parses the HTML to extract details like movie ID, title, year, and rating, and formats the first 50 results into a **JSON** structure.
- **Why you need it:** This simulates a content acquisition task for a streaming service.It's a fundamental web scraping skill essential for gathering structured data from dynamic websites, handling HTML parsing, and formatting data for use in other applications.

### **Question 3: Wikipedia Outline**

- **What it Covered:** Building a web API using **FastAPI** in Python. The API accepts a country name as a `GET` query parameter, constructs the URL for that country's English Wikipedia page, fetches and parses the HTML using `BeautifulSoup` to find all heading tags (`<h1>` to `<h6>`), and returns them as a structured **Markdown outline** in a plain text response.
- **Why you need it:** This simulates a service for an educational platform.It teaches how to build a simple, data-driven API, combine web scraping with a web framework, and dynamically generate content in a specific, non-JSON format (Markdown).

### **Question 4: Scrape the BBC Weather API**

- **What it Covered:** Writing a **Python** script with `requests` to fetch a multi-day weather forecast. This required a two-step process: first, querying the BBC's locator service to find the unique `locationId` for a city, and second, using that ID to query the weather broker API to get the actual forecast data, which is then formatted as a **JSON** object.
- **Why you need it:** This simulates a data integration task for an agricultural tech company.It demonstrates how to reverse-engineer and interact with undocumented or internal JSON APIs, a crucial skill for data gathering when a formal, public API is not available.

### **Question 5: Find the bounding box of a city**

- **What it Covered:** Writing a **Python** script using `requests` to query the **Nominatim API**, which is based on OpenStreetMap data. The script searches for a city and country, parses the JSON response to find the correct result (where `addresstype` is "city"), and extracts the `boundingbox` array to return either the minimum or maximum latitude.
- **Why you need it:** This simulates a task for a logistics company defining its service zones.It shows how to use public geospatial APIs to retrieve precise geographical data, filter complex JSON responses for the most relevant information, and extract specific data points.

### **Question 6: Search Hacker News**

- **What it Covered:** Writing a **Python** script using `requests` and the built-in `xml.etree.ElementTree` library. The script queries the HNRSS service, which provides custom **RSS feeds** for Hacker News, by constructing a URL with search and minimum points parameters. It then fetches the **XML** data, parses the tree to find the first `<item>`, and extracts its `<link>` text.
- **Why you need it:** This simulates a task for a market research firm monitoring tech trends.It's a key skill for data extraction from non-HTML/JSON sources, demonstrating how to consume and parse structured XML data from RSS feeds.

### **Question 7: Find newest GitHub user**

- **What it Covered:** Using the **GitHub REST API** with `requests` to find the newest user from a specific location and with a minimum number of followers. This requires a two-step API process: first, calling the search API with `sort=joined` to find the newest user's profile `url`, and second, making a request to that user's profile URL to get the precise `created_at` timestamp.
- **Why you need it:** This simulates a recruitment task for identifying emerging tech talent.It teaches advanced API interaction, including using search parameters, sorting results, and handling multi-step data retrieval where one API call's output is the input for the next.

### **Question 8: Create a Scheduled GitHub Action**

- **What it Covered:** Creating a **GitHub Action** workflow YAML file inside a `.github/workflows/` directory. The workflow is configured to trigger on a `schedule` (using `cron` syntax) and also manually via `workflow_dispatch`. The job's steps check out the repository, run a shell command to update a file with the current date, and then commit and push the change back to the repository.
- **Why you need it:** This simulates a DevOps task for automating daily repository activity and tracking.It's a foundational skill in CI/CD and automation, showing how to schedule tasks, manage repository state, and automate commits using GitHub's built-in tools.

### **Question 9: Extract tables from PDF**

- **What it Covered:** Writing a **Python** script that uses `tabula-py` (which requires Java) to read tables from a multi-page PDF document. The extracted data is concatenated into a single `pandas` DataFrame, cleaned, and then filtered based on specific criteria (e.g., score >= 80 in 'Physics') to calculate the sum of marks in another subject for the filtered students.
- **Why you need it:** This simulates a data analysis task for processing academic reports.It demonstrates how to extract structured data from unstructured or "dark data" sources like PDFs, a critical and often challenging data-wrangling skill.

### **Question 11: Count crawled HTML files**

- **What it Covered:** Using the command-line tool **`wget`** to perform a recursive crawl of a website. The command used options like `--recursive`, `--level=inf`, and `--accept html,htm` to download all linked HTML files. Afterwards, a chain of shell commands (`find`, `grep`, `wc`) was used to filter and count the number of downloaded filenames that start with a letter within a specified alphabetical range.
- **Why you need it:** This simulates a task for a research tool estimating the workload for processing a site.It teaches how to use powerful command-line tools for web crawling and data processing, a fundamental skill for system administration and data engineering pipelines.

### **Question 12: Convert HTML Table to Markdown**

- **What it Covered:** Writing a **Python** script using `requests` to fetch a webpage, `beautifulsoup4` to parse the HTML and find the `<table>` element, and the `markdownify` library to convert that HTML table element directly into a **Markdown table** string.
- **Why you need it:** This simulates a service that aggregates HTML reports into a format suitable for version control or documentation.It's a practical automation skill for data conversion, report generation, and content migration from the web to Markdown-based systems.

### **Question 13: Sum Table Values with Playwright**

- **What it Covered:** Writing a **Python** script using **Playwright** to automate a headless browser. The script loops through a list of URLs, navigates to each page, and waits for tables that are generated dynamically by **JavaScript** to load. It then uses `page.locator("td")` to find all table cells, extract their text, and calculate the total sum of all numerical values across all pages.
- **Why you need it:** This simulates a quality assurance task for validating data in dynamic web reports.It teaches how to scrape "client-side rendered" websites where simple tools like `requests` fail, a critical skill for interacting with modern, JavaScript-heavy web applications.

## To learn more about these

**Spreadsheet Scraping**

- [Scraping with Excel](https://tds.s-anand.net/#/scraping-with-excel.md)
- [Scraping with Google Sheets](https://tds.s-anand.net/#/scraping-with-google-sheets.md)

**CLI and API Tools**

- [Crawling with the CLI](https://tds.s-anand.net/#/crawling-cli.md)
- [BBC Weather API with Python](https://tds.s-anand.net/#/bbc-weather-api-with-python.md)
- [Nominatim API with Python](https://tds.s-anand.net/#/nominatim-api-with-python.md)
- [Wikipedia Data with Python](https://tds.s-anand.net/#/wikipedia-data-with-python.md)

**Web Automation**

- [Scraping IMDb with JavaScript](https://tds.s-anand.net/#/scraping-imdb-with-javascript.md)
- [Web Automation with Playwright](https://tds.s-anand.net/#/web-automation-with-playwright.md)

**Document Processing**

- [Scraping PDFs with Tabula](https://tds.s-anand.net/#/scraping-pdfs-with-tabula.md)
- [Convert PDFs to Markdown](https://tds.s-anand.net/#/convert-pdfs-to-markdown.md)
- [Convert HTML to Markdown](https://tds.s-anand.net/#/convert-html-to-markdown.md)

**AI Scraping**

- [LLM Website Scraping](https://tds.s-anand.net/#/llm-website-scraping.md)
- [LLM Video Screen-Scraping](https://tds.s-anand.net/#/llm-video-screen-scraping.md)

**Advanced Techniques**

- [Scheduled Scraping with GitHub Actions](https://tds.s-anand.net/#/scheduled-scraping-with-github-actions.md)
- [Scraping emarketer.com](https://tds.s-anand.net/#/scraping-emarketer.md)
- [Scraping: Live Sessions](https://tds.s-anand.net/#/scraping-live-sessions.md)
