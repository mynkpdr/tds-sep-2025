# 1. Import HTML to Google Sheets (0.25 Marks)

## 1. Problem Description

The task is to analyze cricket batting statistics from ESPN Cricinfo using Google Sheets. Specifically, you need to navigate to a designated page of One Day International (ODI) batting stats and calculate the total number of "ducks" (instances where a player is out with a score of zero) listed on that page.

This project simulates a real-world task for a sports analytics firm that needs to efficiently gather and analyze player performance data from web sources.

## 2. Understanding the Requirements

- **Tool**: Google Sheets.
- **Function**: You must use the `=IMPORTHTML()` function.
- **Data Source**: A specific page of the ESPN Cricinfo ODI batting stats website. The exact page number is provided in the problem.
- **Task**:
  1. Import the main data table from the specified URL into a Google Sheet.
  2. Identify the column that lists the number of ducks (this column is labeled "0").
  3. Calculate the sum of all values in that column.
  4. Submit the final sum as the answer.

## 3. Step-by-Step Solution

Let's assume the problem assigned you **page number `6`**.

### Step 1: Construct the URL

First, create the correct URL for the specified page. The base URL is `https://stats.espncricinfo.com/stats/engine/stats/index.html?class=2;template=results;type=batting`. You need to add the page number to it.

The final URL will be:
`https://stats.espncricinfo.com/stats/engine/stats/index.html?class=2;page=6;template=results;type=batting`

### Step 2: Open Google Sheets and Use IMPORTHTML

1. Open a new Google Sheet at [sheets.new](https://sheets.new).
2. Click on cell `A1`.
3. Enter the `IMPORTHTML` formula. This formula takes three arguments:
   - `url`: The URL you constructed.
   - `query`: The type of element to import ("table" or "list"). We need a "table".
   - `index`: The index of the table on the page. On the Cricinfo page, the main data table is the 3rd one.

   Your formula will look like this:

   ```excel
   =IMPORTHTML("https://stats.espncricinfo.com/stats/engine/stats/index.html?class=2;page=6;template=results;type=batting", "table", 3)
   ```

4. Press **Enter**. Google Sheets will fetch the data and populate the cells. You may need to grant access for it to fetch data from an external website.

### Step 3: Find the "Ducks" Column and Calculate the Sum

1. Once the data is loaded, look at the header row (Row 1) to find the column titled **"0"**. This column represents the number of ducks. Let's assume this is **Column M**.
2. In an empty cell (e.g., `N1`), use the `SUM` formula to add up all the numbers in that column.

   Your formula will be:

   ```excel
   =SUM(M2:M)
   ```

   _(This sums everything from cell M2 to the end of Column M.)_

3. Press **Enter**. The cell will now display the total number of ducks, which is your answer.

## 4. How to Verify

- Double-check that you are using the correct page number in the URL.
- Ensure you have identified the correct table index (it should be `3`).
- Confirm that the column you are summing is labeled "0".
- The final number in your `SUM` cell is the answer to submit.
