# 11. Count crawled HTML files (1 Marks)

## 1. Problem Description

The task is to use a **command-line tool (`wget`)** to crawl a given starting URL, recursively download all HTML files from that page and its linked pages, and then count how many of those filenames start with a letter within a specified alphabetical range (for example, from `'N'` to `'Y'`).

This simulates a task for “SiteScout,” a market research tool that estimates the workload required for processing competitor websites by identifying and counting relevant HTML pages.

## 2. Understanding the Requirements

- **Tool**: `wget` (Command-Line Website Downloader).
- **Environment**: Any system with access to Bash or terminal.
- **Input**:
  - A starting URL to begin the crawl.
  - A start letter (e.g., `'S'`).
  - An end letter (e.g., `'U'`).
- **Logic**:
  1. Use `wget` to recursively download all `.html` and `.htm` files starting from the given URL.
  2. Store the files locally in their respective directory structure.
  3. Use shell commands like `find`, `grep`, and `wc` to filter and count the downloaded HTML filenames.
  4. Print the total number of matching files.
- **Output**:
  The total count of HTML files whose filenames start with a letter within the specified range.

## 3. Step-by-Step Solution

### Step 1: Set Up Environment

1. Open your terminal.
2. Verify that `wget` is installed by running:

   ```bash
   wget --version
   ```

   If it’s not installed, you can add it using:

   ```bash
   sudo apt install wget        # For Ubuntu/Debian
   brew install wget            # For macOS
   ```

### Step 2: Crawl and Download All HTML Files

Use the following `wget` command to recursively crawl and download all `.html` pages from the target website:

```bash
wget \
  --recursive \
  --level=inf \
  --no-parent \
  --convert-links \
  --adjust-extension \
  --accept html,htm \
  https://sanand0.github.io/tdsdata/crawl_html/index.html
```

#### Explanation of Options

| Option               | Description                                                                  |
| -------------------- | ---------------------------------------------------------------------------- |
| `--recursive`        | Enables recursive crawling of linked pages.                                  |
| `--level=inf`        | Sets unlimited recursion depth to ensure all linked HTML files are captured. |
| `--no-parent`        | Prevents `wget` from moving above the starting directory.                    |
| `--convert-links`    | Rewrites links for offline browsing.                                         |
| `--adjust-extension` | Ensures all pages are saved with `.html` extensions.                         |
| `--accept html,htm`  | Restricts downloads to `.html` and `.htm` files.                             |

### Step 3: Verify Downloaded Files

After running the command, a folder structure similar to the one below will be created:

```
sanand0.github.io/
└── tdsdata/
    └── crawl_html/
        ├── index.html
        ├── involve.html
        ├── husband.html
        ├── hospital/
        │   └── history.html
        ├── investment/
        │   └── both.html
        └── itself/
            └── nearly.html
```

You can list all the downloaded HTML files using:

```bash
find sanand0.github.io -type f -name "*.html"
```

---

### Step 4: Count Files Within the Alphabetical Range

To count how many HTML filenames start with letters between `'N'` and `'Y'`, run the following command:

```bash
find sanand0.github.io -type f -name "*.html" -printf "%f\n" | grep -E '^[N-Yn-y]' | wc -l
```

## 4. Example Output

After running the commands, you should see output similar to:

```
59
```

This indicates that there are **59 HTML files** whose names start with a letter between **‘N’** and **‘Y’**.

---

## 5. How to Run

1. Copy and paste the `wget` command into your terminal to perform the crawl.
2. Once the crawl is complete, run the `find` and `grep` commands to count the matching files.
3. The terminal will print both the matching filenames (if desired) and the total count.
