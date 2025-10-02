# 11. Multi-cursor edits to convert to JSON (0.4 Marks)

Objective
---------

Use a text editor's multi-cursor feature to efficiently convert a `key=value` formatted text file into a single, minified JSON object, and then find its hash.

Steps to Get the Answer
-----------------------

1. **Download and Open the File:**

    - Save the `q-multi-cursor-json.txt` file provided with this guide.

    - Open it in a powerful text editor like Visual Studio Code, which has excellent multi-cursor support.

2. **Use Multi-Cursor Editing in VS Code:**

    - **Step A: Add Quotes Around Keys:**

        - Place your cursor at the beginning of the first line.

        - Press `Ctrl+Alt+Down` (Windows/Linux) or `Cmd+Opt+Down` (macOS) repeatedly until you have a cursor on every line.

        - Type `"` to add a quote at the beginning of every key.

    - **Step B: Replace `=` with `":"`:**

        - Press `Ctrl+H` (Windows/Linux) or `Cmd+Opt+F` (macOS) to open the Find/Replace tool.

        - In the "Find" box, type `=`.

        - In the "Replace" box, type `":"`.

        - Click "Replace All".

    - **Step C: Add a Quote and Comma at the End of Each Line:**

        - Place your cursor at the end of the first line.

        - Use `Ctrl+Alt+Down` or `Cmd+Opt+Down` again to add a cursor to the end of every line.

        - Type `",` to add a closing quote and a comma.

    - **Step D: Wrap in Curly Braces and Minify:**

        - Select all the text (`Ctrl+A` or `Cmd+A`).

        - Remove all line breaks to make it a single line. A quick way is to use Find/Replace: find `\n` (with regex mode enabled) and replace with nothing.

        - Add an opening curly brace `{` at the very beginning and a closing brace `}` at the very end.

        - Remove the trailing comma from the last entry.

      ## Alternative method

        - If you prefer, you can use the provided Python script `convert.py` to automate this process.

        1. Ensure the input file (`q-multi-cursor-json.txt`) is in the same folder as the script
        2. Run `convert.py`
        3. The script will automatically:
            - Read the input file
            - Convert to JSON format
            - Display the JSON string to copy

            Input file format:

            ```json
            key1=value1
            key2=value2
            ...

            ```

            Output JSON format:

            ```json
            {"key1":"value1","key2":"value2",...}
            ```

3. **Hash the JSON:**

    - Go to the website [tools-in-data-science.pages.dev/jsonhash](https://tools-in-data-science.pages.dev/jsonhash "null").

    - Paste your final, minified JSON string into the text area.

    - Click the "Hash" button.

4. **Submit the Answer:**

    - The website will display the SHA256 hash. Copy this hash and paste it into the answer box.

1. **Save the Data:**

    - Save the large JSON array provided in the quiz prompt to a file named `products.json`.

2. **Run the Python Script:**

    - Use the provided `solve.py` script. It will load the data, perform the filtering and sorting, and print the final minified JSON string.

    - Run it from your terminal: `python solve.py`

3. **Copy the Output:**

    - The script will print a single, long line of minified JSON. This is your answer.

4. **Submit the Answer:**

    - Paste the minified JSON string into the answer box.
