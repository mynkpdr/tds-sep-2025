# 10. dbt: Operations performance mart (1 Mark)

## 1. Problem Description

The task is to write a **dbt SQL model** for **Orbit Ops**. The operations team needs a dashboard, and you are building the "mart" (or "intermediate") model to power it.

Your goal is to write a complete `.sql` file that uses dbt's **Jinja** templating (`{{ config }}` and `{{ ref }}`) to aggregate data from staging tables, filter for a recent time period, and compute a specific business metric at a daily or weekly grain.

## 2. Understanding the Requirements

  - **Tool**: **dbt (data build tool)**.
  - **Language**: SQL + Jinja.
  - **Input**: Upstream dbt models (e.g., `stg_shipments`, `stg_returns`), referenced using `{{ ref('stg_shipments') }}`.
  - **Logic**:
    1.  **Configuration**: Start the file with a `{{ config(...) }}` block to set materialization (e.g., `table` or `view`).
    2.  **Source Data**: Use `WITH` clauses to `SELECT` from one or more `{{ ref(...) }}` models.
    3.  **Filtering**: Filter the data to the **last X days** (e.g., `WHERE date_column >= DATEADD('day', -14, CURRENT_DATE())`).
    4.  **Aggregation**: Use `GROUP BY` to aggregate the data to the required **grain** (e.g., `daily` or `weekly`). Use `DATE_TRUNC('day', ...)` or `DATE_TRUNC('week', ...)` for this.
    5.  **Metrics**: Compute the specific metric required by the question (e.g., `delayed_shipments`, `avg_transit_days`).
    6.  **Cleanup**: Handle `NULL` values using `COALESCE(..., 0)`.
    7.  **Final Select**: Select the final, clean columns, `ORDER BY` the date.
  - **Output**: A complete dbt model as a single block of SQL/Jinja code.

## 3. Step-by-Step Solution

### Step 1: Identify Key Parameters

  - **Model Type**: "mart model" or "intermediate model"? This influences `{{ config }}`.
  - **Domain**: "fulfillment", "inventory", etc. This tells you which `stg_` models to `ref` (e.g., `stg_shipments`).
  - **Metric**: "delayed\_shipments", "stockouts", etc. This defines your `COUNT` or `AVG` logic.
  - **Grain**: "daily" or "weekly". This defines your `DATE_TRUNC` and `GROUP BY`.
  - **Time Window**: "last X days". This defines your `WHERE` clause.

### Step 2: Build the Model

1.  **Start with `config`**:
    `{{ config(materialized='table', freshness=...) }}`
2.  **Add Author Comment (Good Practice)**:
    `-- Author: 23f3004197@ds.study.iitm.ac.in`
3.  **`source_data` CTE**:
    `WITH source_data AS ( SELECT * FROM {{ ref('stg_shipments') }} )`
4.  **`filtered_data` CTE**:
    `filtered_data AS ( SELECT * FROM source_data WHERE shipment_date >= DATEADD('day', -14, CURRENT_DATE()) )`
5.  **`aggregated_data` CTE**:
      - `DATE_TRUNC('week', shipment_date) AS shipment_week`
      - `COUNT(DISTINCT shipment_id) AS total_shipments`
      - `COUNT(CASE WHEN ... THEN shipment_id END) AS delayed_shipments`
      - `GROUP BY 1`
6.  **Final `SELECT`**:
      - `SELECT * FROM aggregated_data ORDER BY shipment_week DESC`

## 4. dbt Model (Example)

*Note: This is an **example** for a "fulfillment" model. You must adapt the logic, refs, and metric calculations to match your specific question.*

```sql
-- Author: 23f3004197@ds.study.iitm.ac.in
{{
    config(
        materialized='table',
        docstore={
            'description': 'Weekly summary of fulfillment performance metrics.'
        }
    )
}}

WITH stg_shipments AS (
    -- 1. Reference upstream staging model
    SELECT * FROM {{ ref('stg_shipments') }}
),

filtered AS (
    -- 2. Filter for the required time window (e.g., last 14 days)
    SELECT *
    FROM stg_shipments
    -- Use CURRENT_DATE to make the model incremental
    WHERE
        date >= DATEADD('day', -14, CURRENT_DATE())
),

aggregated AS (
    -- 3. Aggregate to the required grain (e.g., weekly)
    SELECT
        -- Truncate to the week
        DATE_TRUNC('week', order_date) AS metric_week,

        -- Reference a domain concept (e.g., 'warehouse')
        warehouse_id,
        
        -- Compute the required metric (e.g., 'delayed_shipments')
        COUNT(DISTINCT shipment_id) AS total_shipments,
        
        COUNT(DISTINCT CASE
            WHEN actual_delivery_date > date THEN shipment_id
        END) AS delayed_shipments,

        -- Handle NULLs
        COALESCE(AVG(DATEDIFF('day', ship_date, actual_delivery_date)), 0) AS avg_transit_days

    FROM filtered
    GROUP BY
        1, 2 -- Group by week and warehouse
)

-- 4. Final BI-ready model
SELECT
    metric_week,
    warehouse_id,
    total_shipments,
    delayed_shipments,
    avg_transit_days,
    
    -- Calculate a percentage
    (delayed_shipments::FLOAT / total_shipments) AS ontime_percentage
    
FROM aggregated
ORDER BY
    metric_week DESC
```

## 5. How to Get the Answer

1.  Read the question carefully to identify all parameters (domain, metric, grain, etc.).
2.  Copy the example model above.
3.  **Edit the model** to match your question's requirements:
      - Change the `{{ ref(...) }}` to the correct staging model.
      - Update the `WHERE` clause for the correct number of days.
      - Update the `DATE_TRUNC` for the correct grain.
      - Change the aggregation logic to calculate the correct metric.
      - Ensure you `GROUP BY` the date grain.
4.  Paste your complete, edited dbt model into the answer box.
