# 20. Calculate variance (0.5 Marks)

Objective
---------

Calculate the **sample variance** for a given array of numbers.

Steps to Get the Answer
-----------------------

The quiz provides a unique JSON file containing an array of 1000 measurements.

1. **Download the JSON File:**

    - Save the `q-calculate-variance.json` file provided.

2. **Use a Python Script (Recommended):**

    - The most reliable method is to use Python's `statistics` library, which correctly calculates the sample variance (using the N-1 denominator, also known as Bessel's correction).

    - Save and run the `calculate.py` script provided here. Make sure it's in the same folder as your JSON file.

    - Run from the terminal: `python calculate.py`

3. **Get the Result:**

    - The script will output the sample variance, rounded to two decimal places

4. **Submit the Answer:**

    - Enter the rounded number into the answer box.

### Alternative Method: Using Excel or Google Sheets

1. **Import the Data:**

    - Open the `.json` file in a text editor.

    - Copy the entire array (including the `[` and `]`).

    - In your spreadsheet, you may need to paste the data and then use a "Text to Columns" feature to separate the numbers if they are pasted into a single cell.

2. **Use the `VAR.S` Function:**

    - Once the numbers are in a single column (e.g., column A), click an empty cell.

    - Enter the formula `=VAR.S(A:A)`. This function specifically calculates the *sample* variance.

    - Format the result to have two decimal places.
