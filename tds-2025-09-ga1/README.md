# Summary of all the questions

### **Question 1: VS Code Version**

* **What it Covered:** Using the **Visual Studio Code shell command (`code`)** to interact with the editor from the terminal to check its status.
* **Why you need it:** Integrating your text editor with your terminal is key to an efficient workflow. The `code` command allows you to open files, manage extensions, and check status directly from the command line, which is essential for scripting and automation.

### **Question 2: GitHub Copilot Extension**

* **What it Covered:** Using the **Visual Studio Code shell command (`code`)** to list all installed **extensions** from the terminal.
* **Why you need it:** This is part of the broader skill of managing your development environment as code. It allows you to script your editor setup, share a consistent list of extensions with a team, and troubleshoot issues from the command line, which is essential for creating reproducible development environments.

### **Question 3: POST HTTP requests with uv**

* **What it Covered:** Making an **API request** from the command line using modern tools. It specifically involved sending a **`POST` request** with a **JSON payload** using **`httpie`**, a user-friendly HTTP client, run via **`uv`**.
* **Why you need it:** Interacting with APIs is a daily task for most developers. You need this skill to test your own APIs, consume data from third-party services, and automate workflows. Using command-line clients is essential for scripting and debugging these interactions.

### **Question 4: Run command with npx**

* **What it Covered:** Using the **Node Package eXecutor (`npx`)** to run a specific version of a command-line tool (`prettier`) without installing it globally. It also demonstrated **command-line piping (`|`)** to send the output of one command directly to another (`sha256sum`).
* **Why you need it:** `npx` is a modern, lightweight way to use tools without cluttering your system, ensuring you use the correct version for each project. Piping is a fundamental command-line skill that lets you create powerful, efficient workflows by chaining simple tools together.

### **Question 5: Use Google Sheets**

* **What it Covered:** Using advanced **spreadsheet functions** in **Google Sheets**, specifically modern dynamic array functions like **`SEQUENCE`**, **`ARRAY_CONSTRAIN`**, and **`SUM`**, to perform a complex calculation in a single cell.
* **Why you need it:** Spreadsheets are a key tool for business and data analysis. Advanced functions allow you to perform powerful calculations on entire datasets dynamically, which is more efficient and less error-prone than manual methods. This is a valuable skill for any role that involves data modeling or analysis.

### **Question 6: Use Excel**

* **What it Covered:** Using **Microsoft Excel's** modern dynamic array functions, such as **`SORTBY`** and **`TAKE`**, to perform multi-step data sorting and filtering within a single formula.
* **Why you need it:** Proficiency in Excel's advanced functions is highly valued in business, finance, and data analysis roles. These functions enable powerful, "in-cell" data processing that is more efficient and maintainable than traditional spreadsheet methods involving many helper columns.

### **Question 7: Use DevTools**

* **What it Covered:** Using **Browser Developer Tools** to inspect a webpage's HTML, find a hidden element, and execute **JavaScript** in the **Console** to extract its value.
* **Why you need it:** DevTools are an indispensable tool for web development, QA, and web scraping. You need this skill to debug HTML/CSS, analyze network requests, test JavaScript snippets, and extract data directly from a live webpage.

### **Question 8: Count Weekend Days**

* **What it Covered:** Performing **date and time calculations** in Python. This involved iterating through a date range and using conditional logic based on the day of the week (`.weekday()`).
* **Why you need it:** Working with dates is a common requirement in business analytics, financial modeling, and logistics. You need this skill to answer questions related to scheduling, time-series data, and business-day calculations.

### **Question 9: Extract JSON from a ZIP**

* **What it Covered:** Basic file management and data extraction. This involved **decompressing a ZIP archive** and then **parsing a simple JSON file** to retrieve the value associated with a specific key.
* **Why you need it:** Data is often distributed in compressed archives to save space. You need to be able to extract these archives and then read their contents programmatically. This is a common first step in almost any data processing pipeline.

### **Question 10: Sort and Filter a JSON Product Catalog**

* **What it Covered:** Programmatically manipulating data from a **JSON** file. This involved **parsing JSON**, applying a numerical **filter** to the data, and performing a **multi-level sort** based on several criteria with both ascending and descending orders.
* **Why you need it:** This is a core data manipulation skill for backend and data engineering roles. APIs and data pipelines constantly process JSON. You need this skill to prepare data for display on a website (like a sorted product list), preprocess it for analysis, or transform it before sending it to another service.

### **Question 11: Multi-cursor edits to convert to JSON**

* **What it Covered:** Using an advanced text editor feature, **multi-cursor editing**, to efficiently transform a block of text from a `key=value` format into a single, minified JSON object.
* **Why you need it:** This is a developer productivity skill. For one-off data cleaning or reformatting tasks, using multi-cursor edits can be significantly faster than writing a dedicated script. It’s a power-user technique that dramatically speeds up manual data manipulation.

### **Question 12: CSS: Featured-Sale Discount Sum**

* **What it Covered:** Using an advanced **CSS selector** (`.featured.sale`) to target elements with multiple specific classes. It also involved using **JavaScript** in the DevTools Console to iterate over the selected elements and aggregate data from their `data-*` attributes.
* **Why you need it:** This is a key skill for front-end development, web scraping, and automated testing. Precise CSS selectors allow you to style or target elements accurately, while running JavaScript in the console is a powerful way to debug or extract data from a live webpage on the fly.

### **Question 13: Process files with different encodings**

* **What it Covered:** Correctly reading and parsing multiple text files, each with a different **character encoding** (**`utf-8`**, **`utf-16`**, **`cp1252`**).
* **Why you need it:** Real-world data is messy and comes from various sources and operating systems. If you can't handle different encodings, your programs will crash or produce corrupted text. This is a crucial skill for building robust data processing applications that work with international data or legacy systems.

### **Question 14: Use GitHub**

* **What it Covered:** Demonstrating a basic **version control** workflow using **Git and GitHub**. This included creating a public repository, adding and committing a file, and sharing a direct "raw" URL to its content.
* **Why you need it:** Git and GitHub are the industry standard for code collaboration. Every developer needs to know how to create repositories, save their work with commits, and share it publicly or with a team.

### **Question 15: Replace across files**

* **What it Covered:** Performing a **bulk find-and-replace** operation across multiple files using both a text editor's GUI and command-line tools like **`sed`**. It also covered generating a **SHA256 hash** from the combined file contents to verify data integrity.
* **Why you need it:** Bulk replacement is a massive time-saver for refactoring code or updating content across a project. Calculating a hash is a critical skill for verifying that files have not been corrupted or tampered with after a batch operation or during transfer.

### **Question 16: Move and rename files**

* **What it Covered:** Performing **batch file system manipulation**. This involved programmatically moving files out of subdirectories into a single folder and then renaming them all according to a complex digit-swapping rule.
* **Why you need it:** Data and digital assets are often stored in disorganized ways. You need this skill to automate the process of cleaning up and standardizing file structures and names, which is a critical step in creating organized datasets and reproducible workflows.

### **Question 17: SQL: Average Order Value**

* **What it Covered:** Writing a **SQL query** using an **aggregate function (`AVG`)** on a calculated column (`quantity * unit_price`). It also involved case-insensitive text filtering in the `WHERE` clause by using the **`LOWER()`** function.
* **Why you need it:** This is a fundamental business intelligence task. You need this skill to extract key performance indicators (KPIs) like Average Order Value from raw database records. Handling case-insensitive data is a common real-world challenge, making functions like `LOWER()` essential for accurate analysis.

### **Question 18: Regex email validation**

* **What it Covered:** Using **Regular Expressions (Regex)** to define a pattern for a valid email format and then using that pattern to count matching strings in a list.
* **Why you need it:** Regex is an extremely powerful tool for validating input data (like emails or phone numbers), parsing logs, and performing complex find-and-replace operations. It is a fundamental skill for any developer or data analyst who works with text data.

### **Question 19: Compare files**

* **What it Covered:** Using the command-line utility **`diff`** to find the differences between two text files and piping its output to **`wc`** to count the differing lines.
* **Why you need it:** Comparing files is an essential task for version control (seeing what changed between commits), debugging (comparing log outputs), and validating data transformations. It is a fundamental skill in software development and systems administration.

### **Question 20: Calculate variance**

* **What it Covered:** Calculating the **sample variance**, a fundamental statistical measure of data dispersion. It highlighted the importance of using the correct function (**`VAR.S`** in spreadsheets or **`statistics.variance`** in Python) that uses the N-1 denominator.
* **Why you need it:** Variance is a core concept in data science and statistics for understanding how spread out a dataset is. Knowing how to calculate it correctly is essential for quality control, financial analysis, and scientific research. It is a foundational data literacy skill.

### **Question 21: SQL: Average salary by department**

* **What it Covered:** A fundamental SQL query pattern using **`GROUP BY`** to categorize data, an aggregate function like **`AVG()`** to summarize each category, **`ROUND()`** to format the output, and **`ORDER BY`** to sort the results.
* **Why you need it:** This is one of the most common and powerful operations in data analysis. It allows you to transform raw data into meaningful, aggregated reports (e.g., total sales per region, average response time per server). This is a foundational skill for any data analyst, scientist, or backend developer.

### **Question 22: LLM Sentiment Analysis**

* **What it Covered:** Structuring a correctly formatted **API request for a Large Language Model (LLM)**. This involved creating a JSON body with a specific model and a `messages` array containing both a **`system` role** (to set context) and a **`user` role** (to ask the question).
* **Why you need it:** As AI becomes more integrated into software, interacting with LLMs via API is a critical skill. You must know how to structure these prompts to control the model's behavior and get reliable results. This system/user message pattern is the standard for building almost any application powered by modern AI.

## To learn more about these

* [VS Code](https://tds.s-anand.net/#/vscode) – A powerful and popular source-code editor developed by Microsoft.
* [GitHub Copilot](https://tds.s-anand.net/#/github-copilot) – An AI-powered pair programmer that provides code suggestions and completions.
* [uv](https://tds.s-anand.net/#/uv) – An extremely fast Python package installer, resolver, and virtual environment manager.
* [npx](https://tds.s-anand.net/#/npx) – A package runner tool for the Node.js ecosystem that executes packages without a global installation.
* [Unicode](https://tds.s-anand.net/#/unicode) – The universal standard for encoding and representing text from diverse languages and scripts.
* [DevTools](https://tds.s-anand.net/#/devtools) – A set of web developer tools built directly into browsers for inspecting, debugging, and profiling websites.
* [CSS Selectors](https://tds.s-anand.net/#/css-selectors) – Patterns used to select and style HTML elements on a webpage.
* [JSON](https://tds.s-anand.net/#/json) – A lightweight, human-readable data-interchange format used for APIs and configuration files.
* [Bash](https://tds.s-anand.net/#/bash) – A popular command-line interpreter and scripting language for controlling Unix-like operating systems.
* [llm](https://tds.s-anand.net/#/llm) – A command-line utility for interacting with Large Language Models directly from the terminal.
* [Excel, Google Sheets](https://tds.s-anand.net/#/spreadsheets) – Powerful spreadsheet applications used for data organization, calculation, and analysis.
* [SQLite](https://tds.s-anand.net/#/sqlite) – A self-contained, serverless SQL database engine ideal for local storage and embedded applications.
* [Git, GitHub](https://tds.s-anand.net/#/git) – The standard for version control (Git) and the leading platform for hosting and collaborating on code (GitHub).
