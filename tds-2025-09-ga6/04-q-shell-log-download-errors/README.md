# 4. Shell: Quantify download failures (0.5 Marks)

## 1. Problem Description

The task is to use **shell commands** (like `grep`, `awk`) to analyze an HTTP access log for **Orbit Commerce**. Finance and partner teams have reported file download failures, and you need to quantify the total number of bytes transferred _only_ for failed `4xx` (client error) responses.

Your goal is to filter the log by multiple criteria (method, path, cluster, referer, date, and status) and then **sum** the `bytes` field for all matching lines.

## 2. Understanding the Requirements

- **Tool**: Unix/Linux Shell (e.g., Bash, Zsh, Git Bash on Windows).
- **Tools**: `grep` (or `rg`), `awk`.
- **Input**: A `.log` file (`q-shell-log-download-errors.log`).
- **Log Format**:
  `2024-05-20T10:30:00Z GET /download/report status=404 bytes=1500 ... referer="https://finance.orbit.example.com" ...`
- **Logic**:
  1.  Download the `.log` file.
  2.  Filter by **HTTP Method**: `GET`.
  3.  Filter by **Path Prefix** (e.g., `/download/report`).
  4.  Filter by **Cluster** (e.g., `cluster=aps1`).
  5.  Filter by **Referer** (e.g., `referer="https://finance.orbit.example.com"`).
  6.  Filter by **Status Code**: `4xx` (e.g., `status=4`).
  7.  **Date Filter (if required)**: Some questions may require filtering for "weekend traffic only" (Saturday or Sunday).
  8.  **Sum Bytes**: For all lines that match, find the `bytes=...` field and sum its value.
- **Output**: The final _total sum_ of bytes as a single number.

## 3. Step-by-Step Solution

### Step 1: Download File and Open Terminal

1.  Download the `q-shell-log-download-errors.log` file.
2.  Open your terminal (e.g., Terminal, iTerm, Git Bash).
3.  `cd` to the directory where you downloaded the file.

### Step 2: Build the Shell Command

1.  **`cat` the file**: `cat q-shell-log-download-errors.log`
2.  **Filter (grep)**: Chain `grep` commands to filter by:
    - `GET` method and Path Prefix: `| grep " GET /download/report"`
    - Cluster: `| grep "cluster=aps1"`
    - Referer: `| grep "referer=\"https://finance.orbit.example.com\""`
    - Status Code: `| grep "status=4"`
3.  **Date Filter and Sum (awk)**: Pipe the results to `awk`.
    - **If NO date filter**: We just need to find the `bytes=` field and sum it.
      `| awk -F'[= ]' '{ for(i=1; i<=NF; i++) { if ($i == "bytes") { total += $(i+1) } } } END { print total }'`
    - **If "weekend only" filter**: We need `awk` to check the date _and_ sum.
      `| awk -F'[T= ]' '{ \ cmd = "date -u -d " $1 " +%A"; \ cmd | getline weekday; \ close(cmd); \ if (weekday == "Saturday" || weekday == "Sunday") { \ for(i=1; i<NF; i++) { if ($i == "bytes") { total += $(i+1) } } \ } \ } END { print total }'`

## 4. Shell Command (Example)

This pipeline combines the steps. **You must change the values** to match your specific question.

_(This example is for a question with NO weekend filter. If your question has a weekend filter, use the second `awk` command from Step 2. This assumes Linux/GNU `date`.)_

```bash
# --- EXAMPLE COMMAND (No Weekend Filter) ---
# Replace all filter values with your question's values

cat q-shell-log-download-errors.log | \
  grep " GET /download/report" | \
  grep "cluster=aps1" | \
  grep "referer=\"https://finance.orbit.example.com\"" | \
  grep "status=4" | \
  awk -F'[= ]' '{ for(i=1; i<=NF; i++) { if ($i == "bytes") { total += $(i+1) } } } END { print total }'
```

## 5. How to Run

1.  Save the log file to a directory.
2.  Open your terminal and `cd` to that directory.
3.  Copy, **edit**, and paste the shell command pipeline above.
4.  Press Enter. The command will output a single number (the total bytes).
5.  This number is your answer.
