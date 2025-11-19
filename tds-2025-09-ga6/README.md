# Summary of all the questions

### **Question 3: Shell: Filter live traffic logs**

- **What it Covered:** Using **shell commands** (`grep`, `awk`, `wc`) to audit a large HTTP request log. The task involved filtering the log based on multiple criteria (method, path, cluster, day of week, time) and counting the successful requests, requiring complex date/time parsing with `awk`.
- **Why you need it:** This simulates a critical on-call task for quantifying live traffic. It's a fundamental skill for log analysis, system monitoring, and capacity verification directly on a server.

### **Question 4: Shell: Quantify download failures**

- **What it Covered:** Using **shell commands** (`grep`, `awk`) to analyze an HTTP access log. The task required filtering by multiple criteria (method, path, cluster, referer, 4xx status) and then using `awk` to parse and **sum** the `bytes` field for all matching failed requests.
- **Why you need it:** This teaches how to aggregate numerical data from logs, not just count lines. It's a key skill for quantifying the business impact of errors (like file download failures) and preparing data for reports.

### **Question 5: OpenRefine: Supplier spend consolidation**

- **What it Covered:** Using **OpenRefine** to clean a messy CSV of supplier invoices. The task involved trimming whitespace, **clustering** to merge inconsistent supplier names, de-duplicating rows based on an ID, using GREL to convert currency text to numbers, and faceting to filter and sum the results.
- **Why you need it:** This is a fundamental data cleaning and preparation skill. It shows how to use a specialized tool to rapidly standardize and clean messy, human-entered data, which is often the most time-consuming part of data analysis.

### **Question 6: JSON: Sensor roll-up analytics**

- **What it Covered:** Writing a **Python** script using `pandas` to process a JSONL file of IoT sensor data. The task involved loading and normalizing nested JSON, filtering out "offline" sensors, converting mixed **Fahrenheit and Celsius** temperatures to a single unit, and calculating an average.
- **Why you need it:** This demonstrates how to handle messy, real-world data. Normalizing mixed units and statuses from nested JSON is a critical skill for IoT, telemetry, and any time-series analysis.

### **Question 7: JSON: Flatten nested customer orders**

- **What it Covered:** Using **Python** and `pandas` to process a deeply nested JSONL file of customer orders. The key task was using `pd.json_normalize` with `record_path` and `meta` to **flatten** the nested `orders` and `items` arrays into a single DataFrame, allowing for filtering and aggregation.
- **Why you need it:** This is a critical skill for working with API responses or document database exports. Flattening nested JSON is the standard technique for transforming complex, hierarchical data into a tabular format required for analysis.

### **Question 8: DuckDB: Inventory turnover diagnostics**

- **What it Covered:** Writing a single, complex **SQL query** for **DuckDB** to analyze inventory. The task involved joining `inventory_movements` and `sku_attributes`, filtering the data, and using **CTEs** and `CASE` statements to calculate five different aggregate metrics (like `net_quantity` and `avg_inbound_unit_cost`) in one query.
- **Why you need it:** This demonstrates how to build a business intelligence dashboard query. Translating complex business logic (like net movement and weighted averages) into efficient SQL with conditional aggregation is a core skill for any data analyst.

### **Question 9: DuckDB: Engagement cohort analysis**

- **What it Covered:** Writing a **SQL query** in **DuckDB** to perform **cohort analysis**. The query used **CTEs** to first define a specific _user cohort_ (e.g., November Enterprise users from Canada) and then join with an `events` table to measure that cohort's engagement during a separate _target month_.
- **Why you need it:** This is a fundamental pattern for product analytics. Understanding how to write queries that isolate a cohort and then measure its subsequent activity is the key to calculating retention, engagement, and lifetime value.

### **Question 10: dbt: Operations performance mart**

- **What it Covered:** Building a **dbt SQL model** to create a performance "mart" for a dashboard. The task involved writing a complete `.sql` file using **Jinja** (`{{ config }}`, `{{ ref }}`) to reference staging tables, filter for a recent time window, and use `DATE_TRUNC` to aggregate metrics to a daily or weekly grain.
- **Why you need it:** This is the core workflow of modern data engineering. This skill demonstrates how to build reusable, production-grade data transformations that power BI dashboards, moving beyond simple one-off analytical queries.

### **Question 12: Reconstruct an image**

- **What it Covered:** Writing a **Python** script using the **Pillow** (PIL) library to reconstruct a scrambled image. The task involved reading a 5x5 grid image and a mapping, creating a new blank image, and looping through all 25 positions to **crop** the correct piece from the source and **paste** it into its destination.
- **Why you need it:** This is a fundamental skill in programmatic image manipulation. It teaches how to work with image coordinates, crop tiles, and re-assemble them, a common task in image processing, data augmentation for AI, and digital forensics.

## To learn more about these

**Excel Preparation**

- [Data Cleansing in Excel](https://tds.s-anand.net/#/data-cleansing-in-excel.md)
- [Data Transformation in Excel](https://tds.s-anand.net/#/data-transformation-in-excel.md)
- [Splitting Text in Excel](https://tds.s-anand.net/#/splitting-text-in-excel.md)
- [Data Aggregation in Excel](https://tds.s-anand.net/#/data-aggregation-in-excel.md)

**Command Line Tools**

- [Data Preparation in the Shell](https://tds.s-anand.net/#/data-preparation-in-the-shell.md)
- [Data Preparation in the Editor](https://tds.s-anand.net/#/data-preparation-in-the-editor.md)

**Database Tools**

- [Data Preparation in DuckDB](https://tds.s-anand.net/#/data-preparation-in-duckdb.md)
- [Data Transformation with dbt](https://tds.s-anand.net/#/dbt.md)

**Specialized Tools**

- [Cleaning Data with OpenRefine](https://tds.s-anand.net/#/cleaning-data-with-openrefine.md)
- [Parsing JSON](https://tds.s-anand.net/#/parsing-json.md)

**Media Processing**

- [Transforming Images](https://tds.s-anand.net/#/transforming-images.md)
- [Extracting Audio and Transcripts](https://tds.s-anand.net/#/extracting-audio-and-transcripts.md)
