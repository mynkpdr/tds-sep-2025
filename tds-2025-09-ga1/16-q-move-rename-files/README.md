# 16. Move and rename files (0.5 Marks)

Objective
---------

Manipulate a directory of files by moving them out of subfolders and renaming them according to a specific digit-swapping rule, then calculate a hash of the result.

Steps to Get the Answer
-----------------------

1. **Download and Unzip:**

    - Extract the `q-move-rename-files.zip` archive. This will create a few folders with randomly named text files inside.

2. **Move All Files to One Folder:**

    - Create a new, empty folder (e.g., `cleaned_files`).

    - Move all the `.txt` files from the subfolders into this new folder. You can do this manually or with a terminal command. From the parent directory:

        ```bash
        # For Linux/macOS
        mkdir cleaned_files
        find . -type f -name "*.txt" -exec mv {} cleaned_files/ \;

        ```

3. **Rename the Files:**

    - In the `cleaned_files` folder, you need to rename every file. The rule is to replace each digit with the next one (0→1, 1→2, ..., 9→0).

    - For example, `a1b9c.txt` becomes `a2b0c.txt`.

    - This is best done with a script. A Python script is provided below.

4. **Run the Renaming Script:**

    - Open a terminal in that folder and run `python rename.py`. It will rename all the files.

        **(Alternative)** Using GNU `rename`

        GNU `rename` lets you use Perl regex, so you can map digits like this:

        `rename 'y/0123456789/1234567890/' *.txt`

    - `y/` is the transliteration operator in Perl.

    - It replaces each digit with the next, wrapping `9→0`.

5. **Calculate the Final Hash:**

    - In the same terminal (Git Bash or WSL on Windows), run the final command:

        ```bash
        grep . * | LC_ALL=C sort | sha256sum
        ```

    - **Explanation:**

        - `grep . *`: Prints the filename and content of every file (e.g., `a2b0c.txt:x`).

        - `LC_ALL=C sort`: Sorts the output lines alphabetically using a standard byte-order.

        - `sha256sum`: Calculates the hash of the sorted output.

6. **Submit the Answer:**

    - The command will produce a single hash. For the files generated for example `d781b212f43a571c411517f8a70f3f20227db043b41dbe62c4a1624c657a731d`.
