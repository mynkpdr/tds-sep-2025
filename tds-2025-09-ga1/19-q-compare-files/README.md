# 19. Compare files (0.2 Marks)

Objective
---------

Determine how many lines are different between two similar text files, `a.txt` and `b.txt`.

Steps to Get the Answer
-----------------------

1. **Download and Unzip:**

    - Extract the `q-compare-files.zip` archive. You will get `a.txt` and `b.txt`. File `b.txt` is a copy of `a.txt` but with a number of "NEW" strings inserted at random places.

2. **Compare the Files:**

    - The goal is to count the number of lines that do not match exactly.

### Method 1: Using a Command-Line Tool (Recommended)

- **`diff` with `wc`:** The `diff` command is perfect for this. The `wc -l` command counts lines.

  - Open a terminal in the folder with the files.

  - Run this command:

    ```bash
    diff a.txt b.txt | wc -l       
    ```

  - This command finds the differences and then counts how many lines of output `diff` produces. For this specific problem structure, this count might be higher than the actual number of differing lines due to how `diff` shows context. A more accurate command might be `diff --suppress-common-lines -y a.txt b.txt | wc -l`.

### Method 2: Using a Python Script (Most Accurate)

This script reads both files and compares them line by line, giving you the exact count.

1. **Run the Script:**

    - In your terminal, run: `python compare.py`

2. **Get the Result:**

    - The script will print the number of different lines

3. **Submit the Answer:**

    - Enter the number into the answer box.
