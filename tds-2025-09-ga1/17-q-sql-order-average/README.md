# 17. SQL: Average Order Value (0.8 Marks)

Objective
---------

Write a SQL query to calculate the average order value for all orders with a `shipped` status, ignoring case.

The Task
--------

You are given a table named `orders` with the following columns:

- `status` (TEXT)

- `quantity` (INTEGER)

- `unit_price` (FLOAT)

The "order value" is defined as `quantity * unit_price`. You need to find the average of this value only for rows where the `status` is 'shipped', 'Shipped', 'SHIPPED', etc.

The Solution Query
------------------

The key is to use `LOWER()` (or `UPPER()`) to handle the case-insensitivity and the `AVG()` aggregate function.

```sql
SELECT
  AVG(quantity * unit_price)
FROM
  orders
WHERE
  LOWER(status) = 'shipped';

```

### Explanation

1. **`SELECT AVG(quantity * unit_price)`**: This calculates the average of the expression `quantity * unit_price`. The database first computes the order value for each selected row, and then `AVG()` computes the average of those values.

2. **`FROM orders`**: This specifies that we are querying the `orders` table.

3. **`WHERE LOWER(status) = 'shipped'`**: This is the filtering condition.

    - `LOWER(status)` converts the `status` of each row to all lowercase letters before the comparison.

    - `= 'shipped'` checks if the lowercase status is exactly 'shipped'. This correctly includes 'Shipped', 'shipped', and 'SHIPPED'.

This single query will give you the precise answer required by the quiz. For `test@example.com`, the expected result is approximately **50.6094**. Your query's result must be within 0.01 of this value.
