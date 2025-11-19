# 7. JSON: Flatten nested customer orders (1 Mark)

## 1. Problem Description

The task is to write a Python script to process a JSONL file of customer data from **Slingshot Cloud**. Each line is a JSON object for a single customer, but it contains *nested arrays* for `orders` and `items` within each order.

Your goal is to "flatten" or "explode" this nested data to analyze individual line items. You must then filter by region, category, channel, and date, and compute the **total quantity** sold.

## 2. Understanding the Requirements

  - **Language**: Python.
  - **Libraries**: `pandas` (or `ijson`, `json`).
  - **Input**: A `.jsonl` file (`q-json-customer-flatten.jsonl`).
  - **Data Structure**:
    ```json
    {
      "customer_id": "CUST-123",
      "region": "North America",
      "orders": [
        {
          "order_id": "ORD-456",
          "order_date": "2024-05-10T...",
          "channel": "Marketplace",
          "items": [
            { "sku": "SKU-789", "category": "Analytics", "quantity": 5 },
            { "sku": "SKU-101", "category": "Security", "quantity": 2 }
          ]
        }
      ]
    }
    ```
  - **Logic**:
    1.  Read the `.jsonl` file.
    2.  **Flatten the data**: Use a method to "explode" the nested arrays so that each *line item* becomes its own row. Each row should contain the parent info (e.g., `customer_id`, `region`, `order_date`, `channel`) and the item info (`category`, `quantity`).
    3.  **Filter**:
          - Filter by `region` (e.g., "North America").
          - Filter by `category` (e.g., "Commerce").
          - Filter by `channel` (e.g., "Marketplace").
          - Filter by `order_date` (e.g., between two dates).
    4.  **Sum**: Calculate the `SUM` of the `quantity` field for all matching rows.
  - **Output**: The final total quantity as a single integer.

## 3. Step-by-Step Solution

### Step 1: Set Up Environment

1.  Create a project folder (e.g., `customer_orders`).
2.  Create and activate a virtual environment.
3.  Install `pandas`: `pip install pandas`.
4.  Create a Python file (e.g., `flatten_orders.py`).
5.  Download the `q-json-customer-flatten.jsonl` file into the same folder.

### Step 2: Write the Python Script

1.  **Import Libraries**: Import `pandas as pd` and `json`.
2.  **Load Data**: We must load the JSONL file line by line first, as `pd.json_normalize` works best on a list of dicts.
3.  **Flatten Data**: This is a perfect use case for `pd.json_normalize()`.
      - We use `record_path=['orders', 'items']` to tell pandas to "explode" the `items` array, which is nested inside the `orders` array.
      - We use `meta=[...]` to tell pandas which parent-level fields to "copy down" to each new flattened row.
4.  **Filter Data**:
      - Convert `order_date` to datetime objects: `pd.to_datetime()`.
      - Apply all the filters from the question (region, category, channel, date range).
5.  **Calculate Result**: On the filtered DataFrame, select the `quantity` column and call `.sum()`.
6.  **Print Result**: Print the final sum.

## 4. Code (`flatten_orders.py`)

```python
import pandas as pd
import json
from datetime import datetime

def analyze_customer_orders(file_path, region, category, channel, start_date, end_date):
    """
    Flattens, filters, and sums customer order data from a JSONL file.
    """
    
    # Load the JSONL file line by line into a list
    records = []
    with open(file_path, 'r') as f:
        for line in f:
            records.append(json.loads(line))
            
    if not records:
        raise ValueError("No data found in file.")

    # --- Replace these with values from your question ---
    TARGET_REGION = region
    TARGET_CATEGORY = category
    TARGET_CHANNEL = channel
    START_DATE = pd.to_datetime(START_DATE_ISO, utc=True)
    END_DATE = pd.to_datetime(END_DATE_ISO, utc=True)
    # ---------------------------------------------------------

    # Flatten the data
    # 'record_path' explodes the nested lists
    # 'meta' brings parent info down to the new rows
    df_flat = pd.json_normalize(
        records,
        record_path=['orders', 'items'],
        meta=[
            'customer_id',
            'region',
            ['orders', 'order_id'],
            ['orders', 'order_date'],
            ['orders', 'channel']
        ],
        errors='ignore' # Ignore customers with no orders
    )

    if df_flat.empty:
        raise ValueError("Data could not be flattened. Check JSON structure.")

    # 1. Convert timestamp column to datetime objects
    df_flat['orders.order_date'] = pd.to_datetime(df_flat['orders.order_date'])

    # 2. Define filter conditions
    region_filter = df_flat['region'] == TARGET_REGION
    category_filter = df_flat['category'] == TARGET_CATEGORY
    channel_filter = df_flat['orders.channel'] == TARGET_CHANNEL
    
    # 3. Time window filter (inclusive)
    date_filter = (df_flat['orders.order_date'] >= START_DATE) & \
                  (df_flat['orders.order_date'] <= END_DATE)
    
    # 4. Combine all filters
    filtered_df = df_flat[region_filter & category_filter & channel_filter & date_filter]

    if filtered_df.empty:
        print("Warning: No records match the specified filters.")
        return 0

    # 5. Sum the 'quantity' column
    total_quantity = filtered_df['quantity'].sum()
    
    return total_quantity

if __name__ == "__main__":
    # --- Replace these with the values from your question ---
    # Example values. Get the real ones from the question text.
    TARGET_REGION = "North America"
    TARGET_CATEGORY = "Commerce"
    TARGET_CHANNEL = "Marketplace"
    START_DATE_ISO = "2024-02-18"
    END_DATE_ISO = "2024-04-12"
    # ---------------------------------------------------------
    
    FILE_NAME = "q-json-customer-flatten.jsonl"

    try:
        total_qty = analyze_customer_orders(
            FILE_NAME, 
            TARGET_REGION, 
            TARGET_CATEGORY, 
            TARGET_CHANNEL, 
            START_DATE_ISO, 
            END_DATE_ISO
        )
        print("\n--- Result ---")
        print(f"Total quantity for matching items: {total_qty}")
        print("----------------\n")
    except FileNotFoundError:
        print(f"Error: Could not find file '{FILE_NAME}'.")
        print("Please download it and place it in the same directory.")
    except (ValueError, KeyError) as e:
        print(f"An error occurred: {e}")
```

## 5. How to Run

1.  Install pandas: `pip install pandas`.
2.  Save the code as `flatten_orders.py`.
3.  Download `q-json-customer-flatten.jsonl` to the same directory.
4.  Modify the `TARGET_REGION`, `TARGET_CATEGORY`, `TARGET_CHANNEL`, `START_DATE_ISO`, and `END_DATE_ISO` variables in the `if __name__ == "__main__":` block to match your question.
5.  Run the script from your terminal:
    ```bash
    python flatten_orders.py
    ```
6.  The script will print the final total quantity.
