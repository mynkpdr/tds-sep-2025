# 6. JSON: Sensor roll-up analytics (1 Mark)

## 1. Problem Description

The task is to write a Python script to process a large JSONL (JSON Lines) file of IoT telemetry data from **ThermalWatch**. Each line is a JSON object representing a sensor reading.

The data is messy: some temperatures are in **Fahrenheit** and some are in **Celsius**, and some readings are from sensors that are `offline` or in `maintenance`.

Your goal is to filter the data for a specific site, device type, and time window, normalize all temperatures to **Celsius**, and compute the average temperature.

## 2. Understanding the Requirements

- **Language**: Python.
- **Libraries**: `pandas` (or `json` and `datetime`).
- **Input**: A `.jsonl` file (`q-json-sensor-rollup.jsonl`).
- **Logic**:
  1.  Read the `.jsonl` file line by line.
  2.  For each line (JSON object):
      - Filter by `site` (e.g., "Plant-02").
      - Filter by `device` (e.g., starts with "boiler").
      - Filter by `captured_at` (e.g., between two UTC timestamps).
      - Filter _out_ records where `status` is "maintenance" or "offline".
  3.  For all _matching_ records:
      - Access the temperature value: `metrics.temperature.value`.
      - Access the unit: `metrics.temperature.unit`.
      - If the unit is `"F"`, convert the value to Celsius: `C = (F - 32) * 5 / 9`.
      - Store the (now) Celsius value.
  4.  Calculate the **average** of all stored Celsius values.
- **Output**: The final average temperature in Celsius, rounded to two decimal places.

## 3. Step-by-Step Solution

### Step 1: Set Up Environment

1.  Create a project folder (e.g., `sensor_rollup`).
2.  Create and activate a virtual environment.
3.  Install `pandas` (which is excellent for JSONL): `pip install pandas`.
4.  Create a Python file (e.g., `analyze_sensors.py`).
5.  Download the `q-json-sensor-rollup.jsonl` file into the same folder.

### Step 2: Write the Python Script

1.  **Import Libraries**: Import `pandas as pd` and `datetime`.
2.  **Define Conversion Function**: Create a function that takes a row, checks the unit, and returns the temperature in Celsius.
3.  **Load Data**: Use `pd.read_json()` with `lines=True` to load the `.jsonl` file.
4.  **Normalize Data**: `pandas` can't easily normalize the nested JSON. It's better to load it and then use `.apply()` to extract the nested values.
    _A better way_: Load the file line-by-line using the `json` library, process, and append to a list. Then create a DataFrame from that list. This is more memory-efficient and handles nesting.
5.  **Filter Data**:
    - Convert the `captured_at` column to datetime objects: `pd.to_datetime(df['captured_at'])`.
    - Apply a filter for `site`.
    - Apply a filter for `device` using `.str.startswith()`.
    - Apply a filter for the date range.
    - Apply a filter for `status`.
6.  **Calculate Result**: On the filtered DataFrame, select your normalized Celsius column and call `.mean()`.
7.  **Print Result**: Print the final mean, formatted to two decimal places.

## 4. Code (`analyze_sensors.py`)

```python
import pandas as pd
import json
from datetime import datetime

def normalize_temperature(row):
    """Converts a temperature reading to Celsius if it's in Fahrenheit."""
    temp = row['metrics.temperature.value']
    unit = row['metrics.temperature.unit']

    if unit == 'F':
        # (F - 32) * 5 / 9
        return (temp - 32) * 5.0 / 9.0
    return temp

def process_sensor_data(file_path, site, device_type, start_utc, end_utc):
    """
    Reads the JSONL file, filters, normalizes, and calculates avg temp.
    """

    # Use pandas to read the JSONL file and normalize the nested structure
    # This is much simpler than manual parsing.

    records = []
    with open(file_path, 'r') as f:
        for line in f:
            records.append(json.loads(line))

    if not records:
        raise ValueError("No data found in file.")

    # Flatten the nested JSON
    # This creates columns like 'metrics.temperature.value'
    df = pd.json_normalize(records)

    # --- Replace these with values from your question ---
    TARGET_SITE = site
    TARGET_DEVICE_TYPE = device_type

    START_TIME = pd.to_datetime(start_utc, utc=True)
    END_TIME   = pd.to_datetime(end_utc, utc=True)
    # ---------------------------------------------------------

    # 1. Convert timestamp column to datetime objects
    df['captured_at'] = pd.to_datetime(df['captured_at'])

    # 2. Define filter conditions
    site_filter = df['site'] == TARGET_SITE
    device_filter = df['device'].str.startswith(TARGET_DEVICE_TYPE)

    # 3. Time window filter (inclusive)
    time_filter = (df['captured_at'] >= START_TIME) & (df['captured_at'] <= END_TIME)

    # 4. Status filter (exclude 'maintenance' and 'offline')
    status_filter = ~df['status'].isin(['maintenance', 'offline'])

    # 5. Combine all filters
    filtered_df = df[site_filter & device_filter & time_filter & status_filter]

    if filtered_df.empty:
        raise ValueError("No records match the specified filters.")

    # 6. Normalize temperature
    filtered_df['temp_celsius'] = filtered_df.apply(normalize_temperature, axis=1)

    # 7. Calculate the average
    average_temp = filtered_df['temp_celsius'].mean()

    return average_temp

if __name__ == "__main__":
    # --- Replace these with the values from your question ---
    # Example values. Get the real ones from the question text.
    TARGET_SITE = "Plant-02"
    TARGET_DEVICE_TYPE = "boiler"
    START_UTC = "2024-08-27T12:27:33.694Z"
    END_UTC = "2024-08-31T23:59:59Z"
    # ---------------------------------------------------------

    FILE_NAME = "q-json-sensor-rollup.jsonl"

    try:
        avg_temp = process_sensor_data(FILE_NAME, TARGET_SITE, TARGET_DEVICE_TYPE, START_UTC, END_UTC)
        print("\n--- Result ---")
        print(f"Average temperature for {TARGET_DEVICE_TYPE} at {TARGET_SITE} is: {avg_temp:.2f} °C")
        print("----------------\n")
    except (FileNotFoundError):
        print(f"Error: Could not find file '{FILE_NAME}'.")
        print("Please download it and place it in the same directory.")
    except (ValueError, KeyError) as e:
        print(f"An error occurred: {e}")
```

## 5. How to Run

1.  Install pandas: `pip install pandas`.
2.  Save the code as `analyze_sensors.py`.
3.  Download `q-json-sensor-rollup.jsonl` to the same directory.
4.  Modify the `TARGET_SITE`, `TARGET_DEVICE_TYPE`, `START_UTC`, and `END_UTC` variables in the `if __name__ == "__main__":` block to match your specific question.
5.  Run the script from your terminal:
    ```bash
    python analyze_sensors.py
    ```
6.  The script will print the final average temperature, rounded to two decimal places.
