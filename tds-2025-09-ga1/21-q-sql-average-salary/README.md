# 21. SQL: Average salary by department (0.7 Marks)

Objective
---------

Write a SQL query to calculate the average salary for each department, round the result, and order the output alphabetically by department.

The Task
--------

You have a table named `employees` with columns `employee_id`, `name`, `department`, and `salary`. Your goal is to produce a table showing each department and its average salary.

The Solution Query
------------------

This requires grouping the data by department and using aggregate functions.

```sql
SELECT
  department,
  ROUND(AVG(salary)) AS average_salary
FROM
  employees
GROUP BY
  department
ORDER BY
  department;
```

### Explanation

1. **`SELECT department, ROUND(AVG(salary)) AS average_salary`**:

    - `department`: Selects the department name.

    - `AVG(salary)`: Calculates the average salary for the employees within each group.

    - `ROUND(...)`: Rounds the calculated average salary to the nearest whole number.

    - `AS average_salary`: Assigns a clear alias to the new calculated column.

2. **`FROM employees`**: Specifies the table to query.

3. **`GROUP BY department`**: This is the crucial part. It groups all rows with the same `department` value together, so `AVG(salary)` calculates the average for each of those groups separately.

4. **`ORDER BY department`**: Sorts the final result set alphabetically by the `department` name (A-Z).

This query will produce the exact format and values required. The validation script checks if your query's output matches the expected rounded averages for each department.
