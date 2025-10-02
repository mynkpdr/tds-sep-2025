# 8. Count Weekend Days (0.3 Marks)

Objective
---------

Calculate the total number of weekend days (Saturdays and Sundays) within a given date range. The date range is personalized for you.

Steps to Get the Answer
-----------------------

You can solve this using various methods:

### Method 1: Using a Python Script (Recommended)

1. **Create a Python file** (e.g., `count_weekends.py`).

2. **Paste and run the code below.** It iterates through each day in the range and counts the weekends.

```python
import datetime

start_date_str = "1980-02-07"
end_date_str = "2014-01-26"

start_date = datetime.date.fromisoformat(start_date_str)
end_date = datetime.date.fromisoformat(end_date_str)

weekend_count = 0
current_date = start_date

while current_date <= end_date:
    # weekday() returns 5 for Saturday and 6 for Sunday
    if current_date.weekday() >= 5:
        weekend_count += 1
    current_date += datetime.timedelta(days=1)

print(f"Total weekend days: {weekend_count}")

```

1. The script will output the answer. For the example dates, the result is `3546`.

### Method 2: Using an Online Date Calculator

1. Search for an "online date duration calculator" that can count weekends.

2. Enter your personalized start and end dates.

3. The tool will calculate the number of Saturdays and Sundays.

### Method 3: Using a Spreadsheet

1. In Excel or Google Sheets, you can use formulas to list all dates in the range and then count how many are weekends. This is more complex but possible with functions like `SEQUENCE` and `WEEKDAY`.
