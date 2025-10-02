# 5. Use Google Sheets (0.4 Marks)

Objective
---------

Calculate the result of a specific formula in Google Sheets. The values in the formula are personalized based on your email.

Steps to Get the Answer
-----------------------

1. **Open Google Sheets:**

    - Go to [sheets.google.com](https://sheets.google.com "null") and open a new spreadsheet.

2. **Get Your Personalized Formula:**

    - The quiz generates a unique formula for you. Example:

        ```xls
        =SUM(ARRAY_CONSTRAIN(SEQUENCE(100, 100, 8, 2), 1, 10))
        ```

3. **Enter the Formula:**

    - Click on any cell (e.g., `A1`) in your spreadsheet.

    - Paste the personalized formula into the cell and press `Enter`.

4. **Get the Result:**

    - Google Sheets will compute the value instantly. For the example formula above, the result is `170`.

5. **Submit the Answer:**

    - Enter the calculated number into the answer box.

### How the Formula Works

- `SEQUENCE(100, 100, 8, 2)`: Creates a 100x100 grid of numbers starting at `8` and increasing by `2` for each cell.

- `ARRAY_CONSTRAIN(..., 1, 10)`: Takes only the first row and the first 10 columns of that grid. The values will be `8, 10, 12, 14, 16, 18, 20, 22, 24, 26`.

- `SUM(...)`: Adds up those 10 numbers.
