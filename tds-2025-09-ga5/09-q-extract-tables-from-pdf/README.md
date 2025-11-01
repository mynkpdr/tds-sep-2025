# 9. Extract tables from PDF (1 Marks)

## 1. Problem Description

The task is to write a Python script that extracts tabular data from a multi-page PDF document containing student marks. After extracting the data, you need to filter it based on specific criteria (a certain score in one subject within a range of student groups) and then calculate the sum of marks in another subject for the filtered students.

This simulates a data analysis task for "EduAnalytics Corp.," which needs to process academic reports provided as PDFs.

## 2. Understanding the Requirements

- **Language**: Python.
- **Libraries**: `tabula-py` (a wrapper for the Tabula-Java tool) and `pandas` (for data manipulation).
- **Input**: A PDF file containing tables of student marks.
- **Logic**:
  1. Read the tables from a specified range of pages in the PDF file using `tabula-py`.
  2. Concatenate the data from all pages into a single `pandas` DataFrame.
  3. Clean the data: ensure column headers are correct and data types are numeric.
  4. Filter the DataFrame based on the given conditions (e.g., students in groups 10-20 who scored >= 80 in 'Physics').
  5. From the filtered data, select the column for the target subject (e.g., 'Maths') and calculate its sum.
- **Output**: The final calculated sum of marks.

## 3. Step-by-Step Solution

### Step 1: Prerequisites (Java Installation)

`tabula-py` is a Python wrapper around a Java tool called Tabula. **You must have Java installed on your system for it to work.**

- **Check for Java**: Open your terminal and run `java -version`. If it's installed, you'll see version information.
- **Install Java**: If not installed, download and install it from the official [Java website](https://www.java.com/en/download/) or using a package manager like `brew` (macOS) or `apt` (Ubuntu).

### Step 2: Set Up Python Environment

1. Create a project folder (e.g., `pdf_extractor`).
2. Set up and activate a virtual environment.
3. Install the necessary Python libraries:

   ```bash
   pip install tabula-py pandas
   ```

4. Download the PDF file from the problem description and save it in your project folder as `student_marks.pdf`.
5. Create a Python file (e.g., `analyze_marks.py`).

## 4. Code (`analyze_marks.py`)

```python
import tabula
import pandas as pd

def analyze_student_marks(pdf_path: str, groups: tuple, filter_subject: str, filter_threshold: int, sum_subject: str) -> int:
    """
    Extracts, filters, and analyzes student marks from a PDF file.

    Args:
        pdf_path (str): The path to the PDF file.
        groups (tuple): A tuple containing the start and end group (page) numbers.
        filter_subject (str): The subject to filter by.
        filter_threshold (int): The minimum score in the filter subject.
        sum_subject (str): The subject for which to sum the marks.

    Returns:
        int: The total sum of marks for the specified subject after filtering.
    """
    start_group, end_group = groups
    print(f"Reading pages {start_group} to {end_group} from '{pdf_path}'...")

    # Use tabula to read tables from the specified page range
    # `pages` is 1-based, matching the group numbers
    dfs = tabula.read_pdf(pdf_path, pages=f"{start_group}-{end_group}", multiple_tables=True, lattice=True)

    if not dfs:
        raise ValueError("No tables found in the specified PDF pages.")

    # Concatenate all extracted tables into a single DataFrame
    full_df = pd.concat(dfs, ignore_index=True)

    # --- Data Cleaning ---
    # The first row is often read as data, so we need to set the column headers correctly.
    # Let's assume the columns are consistently named Maths, Physics, etc.
    # In some cases, you might need to manually set columns:
    # full_df.columns = ["Maths", "Physics", "English", "Economics", "Biology"]

    # Convert all columns to numeric, coercing errors to NaN (which we can then handle)
    for col in full_df.columns:
        full_df[col] = pd.to_numeric(full_df[col], errors='coerce')

    # Drop rows with any missing values that might result from coercion
    full_df.dropna(inplace=True)

    print(f"Successfully extracted and cleaned {len(full_df)} student records.")

    # --- Filtering ---
    print(f"Filtering for students with '{filter_subject}' >= {filter_threshold}...")
    filtered_df = full_df[full_df[filter_subject] >= filter_threshold]

    print(f"Found {len(filtered_df)} students matching the criteria.")

    # --- Calculation ---
    if sum_subject not in filtered_df.columns:
        raise ValueError(f"Subject '{sum_subject}' not found in the table.")

    total_marks = filtered_df[sum_subject].sum()

    return int(total_marks)


if __name__ == "__main__":
    PDF_FILE = "q-extract-tables-from-pdf.pdf"
    # --- Replace these with the values from your question ---
    GROUP_RANGE = (1, 24)  # e.g., groups 1-24
    FILTER_SUBJECT = "Maths"
    FILTER_SCORE = 21
    SUM_SUBJECT = "English"
    # ---------------------------------------------------------

    try:
        total = analyze_student_marks(
            pdf_path=PDF_FILE,
            groups=GROUP_RANGE,
            filter_subject=FILTER_SUBJECT,
            filter_threshold=FILTER_SCORE,
            sum_subject=SUM_SUBJECT
        )
        print("\n--- Result ---")
        print(f"Total '{SUM_SUBJECT}' marks for the filtered students: {total}")
        print("----------------\n")
    except (FileNotFoundError, ValueError) as e:
        print(f"An error occurred: {e}")
        print("Please ensure Java is installed and the PDF file is in the same directory.")
```

## 5. How to Run

1. Make sure you have **Java** installed.
2. Install `tabula-py` and `pandas`.
3. Download the PDF provided in the question and save it as `student_marks.pdf` in the same folder as your script.
4. Save the code as `analyze_marks.py`.
5. Update the configuration variables at the bottom of the script to match your specific question's parameters.
6. Run the script from your terminal:

   ```bash
   python analyze_marks.py
   ```

7. The script will output the final sum, which is your answer.
