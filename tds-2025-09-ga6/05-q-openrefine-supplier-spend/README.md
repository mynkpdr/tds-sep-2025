# 5. OpenRefine: Supplier spend consolidation (1 Mark)

## 1. Problem Description

The task is to use **OpenRefine** to clean a messy CSV export of supplier invoices for **Orbit Commerce**. The procurement team's data suffers from inconsistent supplier names (e.g., "Astra Supplies", "AstraSupply"), duplicate invoice IDs, and currency text mixed with numbers.

Your goal is to clean, de-duplicate, and standardize the data, then filter for a specific subset and calculate the total approved spend.

## 2. Understanding the Requirements

- **Tool**: **OpenRefine**.
- **Input**: A `.csv` file (`q-openrefine-supplier-spend.csv`).
- **Data Issues**:
  - `supplier_name`: Inconsistent, needs clustering.
  - `invoice_id`: May have duplicates.
  - `amount_usd`: Text strings with currency (e.g., `$1,234.56`, `USD 500`).
- **Logic**:
  1.  Download the `.csv` file.
  2.  Create a new project in OpenRefine.
  3.  **Trim Whitespace**: On all text columns (`supplier_name`, `category`, `status`).
  4.  **Cluster Suppliers**: Use OpenRefine's **Clustering** feature on the `supplier_name` column (e.g., "key collision" or "nearest neighbor") to find and merge all variations into their canonical names.
  5.  **De-duplicate Invoices**: On the `invoice_id` column, sort by `comment` (to keep the "cleanest" one) and then **Facet** -> **Customized Facets** -> **Duplicates**. Select "true" and remove the duplicate rows.
  6.  **Clean Amount**: On the `amount_usd` column, use a GREL (General Refine Expression Language) transform to remove currency symbols and convert to a number.
  7.  **Filter Data**: Create text facets for `supplier_name`, `category`, and `status`. Select the specific values required by the question (e.g., "Astra Supplies", "Hardware", "Approved").
  8.  **Sum Result**: With the data filtered, view the `amount_usd` (cleaned) column. OpenRefine will show the sum of the numeric column at the top of the facet or column dropdown.
- **Output**: The final summed spend as a single number.

## 3. Step-by-Step Solution (using OpenRefine)

### Step 1: Create Project

1.  Download `q-openrefine-supplier-spend.csv`.
2.  Open OpenRefine. On the welcome screen, click **Create Project** -> **This Computer**.
3.  Choose the `.csv` file and click **Next**.
4.  Ensure the data looks correct in the preview (e.g., check that "Parse next 1 lines as header" is checked).
5.  Click **Create Project**.

### Step 2: Clean and Standardize

1.  **Trim Whitespace**:
    - On the `All` column (or text columns): **Dropdown Menu > Edit cells > Common transforms > Trim leading and trailing whitespace**.
2.  **Cluster Suppliers**:
    - On the `supplier_name` column: **Dropdown > Facet > Text facet**.
    - In the new facet box on the left, click the **Cluster** button.
    - In the popup, select different **Methods** (e.g., "key collision") to find groups.
    - Check the **Merge** box for each group you want to combine and click **Merge Selected & Re-Cluster**. Repeat until all aliases are merged into their canonical names.
3.  **De-duplicate Invoices**:
    - On the `invoice_id` column: **Dropdown > Sort...** -> **text (a-z)**.
    - On the `invoice_id` column: **Dropdown > Facet > Customized facets > Duplicates**.
    - In the "Duplicates" facet on the left, select **true**.
    - On the **All** column: **Dropdown > Edit rows > Remove Duplicate rows**. Select "invoice_id" as the key column.
    - Close the "Duplicates" facet.
4.  **Clean Amount**:
    - On the `amount_usd` column: **Dropdown > Edit cells > Transform...**
    - In the "Expression" box, enter this GREL:
      `value.replace(/[^0-9.]/, "").toNumber()`
    - Click **OK**.
    - On the `amount_usd` column: **Dropdown > Edit cells > Common transforms > To number**.

### Step 3: Filter and Get Answer

1.  **Filter `status`**:
    - On the `status` column: **Dropdown > Facet > Text facet**.
    - In the facet box, click on **"Approved"**.
2.  **Filter `supplier_name`**:
    - On the `supplier_name` column: **Dropdown > Facet > Text facet**.
    - In the facet box, click the canonical name from your question (e.g., "Astra Supplies").
3.  **Filter `category`**:
    - On the `category` column: **Dropdown > Facet > Text facet**.
    - In the facet box, click the category from your question (e.g., "Hardware").
4.  **Get Sum**:
    - Look at the top of the `amount_usd` column. OpenRefine automatically shows the `sum` for the filtered, numeric data.
    - _Alternatively_, export the filtered data to CSV and sum the `amount_usd` column in a spreadsheet application.

## 4. How to Get the Answer

1.  Follow all the cleaning, clustering, and filtering steps above.
2.  The final **sum** shown by OpenRefine for the `amount_usd` column (after filtering) is your answer.
3.  Enter this number (e.g., `49643.19`) into the answer box.
