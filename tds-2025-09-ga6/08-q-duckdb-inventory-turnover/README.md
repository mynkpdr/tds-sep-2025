# 8. DuckDB: Inventory turnover diagnostics (1 Mark)

## 1. Problem Description

The task is to write a single **SQL query** for **DuckDB** to analyze inventory movements for **Orbit Fulfillment**. You have access to two tables: `inventory_movements` (a log of all transactions) and `sku_attributes` (metadata about each item).

Your goal is to write a query that filters for a specific category, location, and date range, and then computes five key aggregate metrics: `sku_count`, `total_inbound`, `total_outbound`, `net_quantity`, and `avg_inbound_unit_cost`.

## 2. Understanding the Requirements

  - **Tool**: **DuckDB** (SQL).
  - **Input**: Two pre-loaded tables:
    1.  `inventory_movements` (sku, location, movement\_type, quantity, unit\_cost, adjustment\_direction, quality\_flag, movement\_date)
    2.  `sku_attributes` (sku, category, safety\_stock, lead\_time\_days)
  - **Logic**:
    1.  **Join** `inventory_movements` with `sku_attributes` on `sku`.
    2.  **Filter** the results based on:
          - `category` (from `sku_attributes`).
          - `location` (from `inventory_movements`).
          - `movement_date` (between two dates, inclusive).
    3.  **Aggregate** the filtered data into a single row.
    4.  **Calculate Metrics**:
          - `sku_count`: Count of *distinct* SKUs.
          - `total_inbound`: Sum of `quantity` where `movement_type = 'INBOUND'`.
          - `total_outbound`: Sum of `quantity` where `movement_type = 'OUTBOUND'`.
          - `net_quantity`: The sum of all quantity changes.
              - Inbound is `+quantity`.
              - Outbound is `-quantity`.
              - Adjustment (where `quality_flag != 'scrap'`) is `+quantity` or `-quantity` based on `adjustment_direction`.
          - `avg_inbound_unit_cost`: The *weighted average* cost of inbound items (`SUM(quantity * unit_cost) / SUM(quantity)`). Must handle division by zero.
    5.  **Exclude `scrap`**: All adjustments where `quality_flag = 'scrap'` should be ignored.
  - **Output**: A single row with exactly five columns: `sku_count`, `total_inbound`, `total_outbound`, `net_quantity`, `avg_inbound_unit_cost`.

## 3. Step-by-Step Solution

### Step 1: Understand the Data

  - We need to join the tables to filter by `category`.
  - We need to use `CASE` statements to handle the different `movement_type` and `adjustment_direction` values.
  - We must filter out `'scrap'` adjustments *before* aggregating.

### Step 2: Build the Query

1.  **CTEs (Common Table Expressions)** are the cleanest way to solve this.
2.  **CTE 1: `filtered_movements`**
      - `JOIN` the two tables.
      - Apply all `WHERE` filters: `category`, `location`, `movement_date`, and `quality_flag != 'scrap'`.
      - Select all the columns you'll need (sku, movement\_type, quantity, unit\_cost, adjustment\_direction).
3.  **CTE 2: `movement_calcs`**
      - Select from `filtered_movements`.
      - Use `CASE` statements to create new columns:
          - `inbound_qty`: `CASE WHEN movement_type = 'INBOUND' THEN quantity ELSE 0 END`
          - `outbound_qty`: `CASE WHEN movement_type = 'OUTBOUND' THEN quantity ELSE 0 END`
          - `adj_qty`: `CASE WHEN movement_type = 'ADJUSTMENT' AND adjustment_direction = 'remove' THEN -quantity WHEN movement_type = 'ADJUSTMENT' THEN quantity ELSE 0 END`
          - `inbound_cost_x_qty`: `CASE WHEN movement_type = 'INBOUND' THEN quantity * unit_cost ELSE 0 END`
4.  **Final `SELECT`**:
      - Select from `movement_calcs`.
      - `COUNT(DISTINCT sku) AS sku_count`
      - `SUM(inbound_qty) AS total_inbound`
      - `SUM(outbound_qty) AS total_outbound`
      - `SUM(inbound_qty - outbound_qty + adj_qty) AS net_quantity`
      - `COALESCE(SUM(inbound_cost_x_qty) / SUM(inbound_qty), 0) AS avg_inbound_unit_cost` (Use `COALESCE` or `CASE` to prevent division by zero).

## 4. SQL Query

*Note: This is a complete, runnable query. You must replace the example filter values with the specific values from your question.*

```sql
-- Replace 'Electronics', 'RTP-1', '2024-01-01', and '2024-07-31'
-- with the values from your question.

WITH filtered_movements AS (
    -- 1. Join and filter data
    SELECT
        m.sku,
        m.movement_type,
        m.quantity,
        m.unit_cost,
        m.adjustment_direction
    FROM
        inventory_movements AS m
    JOIN
        sku_attributes AS s ON m.sku = s.sku
    WHERE
        s.category = 'Electronics' -- <-- Replace this
        AND m.location = 'RTP-1' -- <-- Replace this
        AND m.movement_date BETWEEN '2024-01-01' AND '2024-07-31' -- <-- Replace dates
        AND m.quality_flag != 'scrap'
),

movement_calcs AS (
    -- 2. Calculate values for each movement
    SELECT
        sku,
        -- Calculate inbound
        CASE
            WHEN movement_type = 'INBOUND' THEN quantity
            ELSE 0
        END AS inbound_qty,
        
        -- Calculate outbound
        CASE
            WHEN movement_type = 'OUTBOUND' THEN quantity
            ELSE 0
        END AS outbound_qty,
        
        -- Calculate adjustments
        CASE
            WHEN movement_type = 'ADJUSTMENT' AND adjustment_direction = 'remove' THEN -quantity
            WHEN movement_type = 'ADJUSTMENT' THEN quantity
            ELSE 0
        END AS adj_qty,

        -- Calculate weighted cost components
        CASE
            WHEN movement_type = 'INBOUND' THEN quantity * unit_cost
            ELSE 0
        END AS inbound_cost_x_qty
    FROM
        filtered_movements
)

-- 3. Aggregate final metrics
SELECT
    COUNT(DISTINCT sku) AS sku_count,
    SUM(inbound_qty) AS total_inbound,
    SUM(outbound_qty) AS total_outbound,
    SUM(inbound_qty - outbound_qty + adj_qty) AS net_quantity,
    
    -- Use COALESCE to handle division by zero if total_inbound is 0
    COALESCE(SUM(inbound_cost_x_qty) / SUM(inbound_qty), 0) AS avg_inbound_unit_cost
FROM
    movement_calcs;
```

## 5. How to Get the Answer

1.  Copy the SQL query above.
2.  **Edit the `WHERE` clause** in the `filtered_movements` CTE to use the exact `category`, `location`, and `movement_date` values provided in your question.
3.  Paste the entire, edited query into the DuckDB answer box and submit.
