# 6. Use Excel (0.5 Marks)

Objective
---------

Calculate the result of a specific formula in Microsoft Excel (Office 365 version). The arrays and values in the formula are personalized.

Steps to Get the Answer
-----------------------

1. **Open Microsoft Excel:**

    - You must use a version of Excel that supports modern array functions like `SORTBY` and `TAKE` (typically Office 365).

2. **Get Your Personalized Formula:**

    - The quiz generates a unique formula. For example:

        ```xls
        =SUM(TAKE(SORTBY({2,8,3,12,8,12,12,1,8,0,11,4,14,1,3,3}, {10,9,13,2,11,8,16,14,7,15,5,4,6,1,3,12}), 1, 4))
        ```

3. **Enter the Formula:**

    - Click on any cell, paste the formula, and press `Enter`.

4. **Get the Result:**

    - Excel will calculate the result. For the example formula, the answer is `20`.

5. **Submit the Answer:**

    - Enter the result into the answer box.

### How the Formula Works

- `SORTBY({2,8,...}, {10,9,...})`: This sorts the first array (`{2,8,...}`) based on the corresponding values in the second array (`{10,9,...}`). The second array acts as a set of sort keys.

- `TAKE(..., 1, 12)`: This takes the first `12` elements from the newly sorted array.

- `SUM(...)`: This adds up those `12` elements.
