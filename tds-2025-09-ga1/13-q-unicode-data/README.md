# 13. Process files with different encodings (0.4 Marks)

Objective
---------

Downloada ZIP file containing three data files with differenttext encodings. Parse all three files and sum a specific column's values based on a set of matching symbols.nd its hash.

Steps to Get
------------

This task is best solved with a scripting language like Python that can handle different text encodings.

the Answer
----------

1. Unzip: and extract the file `q-unicode-data.zip`  archive. You will get three files:  `data1.csv`,  `data2.csv`, and `data3.txt`
    - `data1.csv` is encoded in `cp1252` (Windows-1252).
    - `data2.csv` is encoded in `utf-8`.
    - `data3.txt` is encoded in `utf-16` and uses tab (`\t`) as a separator.
2. **Identify the Symbols:**

    - The symbols to look for are generated uniquely for you.

3. **Run the Python Script:**

    - Use the provided `main.py` script. It is designed to:

        - Read `data1.csv` using `cp1252` encoding.

        - Read `data2.csv` using `utf-8` encoding.

        - Read `data3.txt` using `utf-16` encoding and tab separators.

        - Sum the `value` column for rows where the `symbol` matches one of the target symbols. Place the script in the same folder as the extracted files and run it:

            ```
            python solve.py
            ```

    - **Get the Result:**

        - The script will give you the total sum.

5. **Submit the Answer:**

    - The total sum will be your answer. Copy and paste it into the answer box.
