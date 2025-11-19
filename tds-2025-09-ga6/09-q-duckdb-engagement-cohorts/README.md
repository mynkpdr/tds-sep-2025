# 9. DuckDB: Engagement cohort analysis (1 Mark)

## 1. Problem Description

The task is to write a single **SQL query** for **DuckDB** to perform cohort analysis for **Prism Analytics**. You have two tables: `user_profiles` (when and where users signed up) and `user_events` (what users do).

Your goal is to build a query that isolates a *specific user cohort* (defined by signup month, plan, and country) and then measures their engagement (retention rate, session count, etc.) during a *specific target month*.

## 2. Understanding the Requirements

  - **Tool**: **DuckDB** (SQL).
  - **Input**: Two pre-loaded tables:
    1.  `user_profiles` (user\_id, signup\_date, cohort\_month, country, plan)
    2.  `user_events` (user\_id, event\_date, event\_type, minutes\_spent, feature)
  - **Logic**:
    1.  **CTE 1: `cohort`**
          - Find all `user_id`s that belong to the *specific cohort* defined in the question (e.g., `cohort_month = '2023-11-01'`, `plan = 'Enterprise'`, `country = 'Canada'`).
    2.  **CTE 2: `cohort_events`**
          - `JOIN` the `cohort` users with the `user_events` table on `user_id`.
          - Filter these events for *only* the `session` event type.
          - Filter these events for *only* the *target engagement month* (e.g., `event_date` between '2024-05-01' and '2024-05-31').
    3.  **CTE 3: `metrics`**
          - Calculate `cohort_users`: `(SELECT COUNT(*) FROM cohort)`.
          - Calculate `retained_users`: `(SELECT COUNT(DISTINCT user_id) FROM cohort_events)`.
          - Calculate `total_sessions`: `(SELECT COUNT(*) FROM cohort_events)`.
          - Calculate `total_minutes`: `(SELECT SUM(minutes_spent) FROM cohort_events)`.
    4.  **Final `SELECT`**:
          - Combine these metrics, using `CASE` or `COALESCE` to prevent division by zero.
          - `active_rate`: `retained_users / cohort_users`
          - `avg_sessions_per_user`: `total_sessions / retained_users`
          - `avg_minutes_per_user`: `total_minutes / retained_users`
  - **Output**: A single row with exactly five columns: `cohort_users`, `retained_users`, `active_rate`, `avg_sessions_per_user`, `avg_minutes_per_user`.

## 3. Step-by-Step Solution

### Step 1: Define Cohort and Target Month

  - Identify the **cohort filters** from the question:
      - `cohort_month` (e.g., '2023-11-01')
      - `plan` (e.g., 'Professional')
      - `country` (e.g., 'Germany')
  - Identify the **target engagement month** from the question:
      - e.g., "during May 2024". This means `event_date` from `2024-05-01` to `2024-05-31`.

### Step 2: Build the Query

1.  **`cohort_users` CTE**: Find all users matching the cohort filters.
2.  **`retained_user_events` CTE**: Find all *session* events from those users *during the target month*.
3.  **`aggregated_metrics` CTE**: Calculate the four base metrics:
      - `cohort_size`: `COUNT(*)` from `cohort_users`.
      - `retained_count`: `COUNT(DISTINCT user_id)` from `retained_user_events`.
      - `session_count`: `COUNT(*)` from `retained_user_events`.
      - `minute_count`: `SUM(minutes_spent)` from `retained_user_events`.
4.  **Final `SELECT`**: Select the metrics and perform the final divisions, using `COALESCE(..., 0)` or `CASE` to handle cases where `retained_count` or `cohort_size` is 0.

## 4. SQL Query

*Note: This is a complete, runnable query. You must replace the example filter values with the specific values from your question.*

```sql
-- Replace '2023-11-01', 'Professional', 'Germany', '2024-05-01', and '2024-05-31'
-- with the values from your question.

WITH cohort_users AS (
    -- 1. Define the user cohort
    SELECT user_id
    FROM user_profiles
    WHERE
        cohort_month = '2023-11-01' -- <-- Replace this
        AND plan = 'Professional' -- <-- Replace this
        AND country = 'Germany' -- <-- Replace this
),

retained_user_events AS (
    -- 2. Find all 'session' events for these users in the target month
    SELECT
        e.user_id,
        e.minutes_spent
    FROM
        user_events AS e
    JOIN
        cohort_users AS c ON e.user_id = c.user_id
    WHERE
        e.event_type = 'session'
        AND e.event_date BETWEEN '2024-05-01' AND '2024-05-31' -- <-- Replace dates
),

aggregated_metrics AS (
    -- 3. Calculate all base metrics in one place
    SELECT
        (SELECT COUNT(*) FROM cohort_users) AS cohort_users,
        COUNT(DISTINCT user_id) AS retained_users,
        COUNT(*) AS total_sessions,
        SUM(minutes_spent) AS total_minutes
    FROM
        retained_user_events
)

-- 4. Final calculation
SELECT
    cohort_users,
    retained_users,
    
    -- Use CASE to prevent division by zero
    CASE
        WHEN cohort_users = 0 THEN 0
        ELSE retained_users::DOUBLE / cohort_users
    END AS active_rate,
    
    CASE
        WHEN retained_users = 0 THEN 0
        ELSE total_sessions::DOUBLE / retained_users
    END AS avg_sessions_per_user,
    
    CASE
        WHEN retained_users = 0 THEN 0
        ELSE total_minutes::DOUBLE / retained_users
    END AS avg_minutes_per_user
FROM
    aggregated_metrics;
```

## 5. How to Get the Answer

1.  Copy the SQL query above.
2.  **Edit the `WHERE` clauses** in the `cohort_users` and `retained_user_events` CTEs to use the exact values provided in your question.
3.  Paste the entire, edited query into the DuckDB answer box and submit.
