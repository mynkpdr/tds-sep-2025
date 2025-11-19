# 3. Shell: Filter live traffic logs (1 Mark)

## 1. Problem Description

The task is to use **shell commands** (like `grep`, `awk`, `cut`) to audit a large HTTP request log for **Orbit Commerce**. You are on-call and need to quantify a specific burst of traffic to verify capacity.

Your goal is to filter the log file based on multiple criteria (HTTP method, path, cluster, day of the week, and time of day) and count the number of _successful_ (2xx) requests that match.

## 2. Understanding the Requirements

- **Tool**: Unix/Linux Shell (e.g., Bash, Zsh, Git Bash on Windows).
- **Tools**: `grep` (or `rg`), `awk`, `wc`.
- **Input**: A `.log` file (`q-shell-log-latency.log`).
- **Log Format**: Each line looks like this:
  `2024-04-17T14:23:11Z GET /api/catalog/items status=200 bytes=32844 ...`
- **Logic**:
  1.  Download the `.log` file.
  2.  Read the log file line by line.
  3.  Filter by **HTTP Method** (e.g., `GET`).
  4.  Filter by **Path Prefix** (e.g., `/api/catalog`).
  5.  Filter by **Cluster** (e.g., `cluster=use1`).
  6.  Filter by **Weekday** (e.g., "Wednesday"). This requires parsing the date.
  7.  Filter by **Time Window** (e.g., between 13:00 and 18:00 UTC).
  8.  Filter by **Status Code** (successful: `status=2..`, i.e., 200-299).
- **Output**: The final _count_ of matching log lines.

## 3. Step-by-Step Solution

### Step 1: Download File and Open Terminal

1.  Download the `q-shell-log-latency.log` file.
2.  Open your terminal (e.g., Terminal, iTerm, Git Bash).
3.  Use `cd` to navigate to the directory where you downloaded the file.

### Step 2: Build the Shell Command

We will pipe several commands together. The main tools are `grep` for simple text matching and `awk` for more complex logic like date/time.

1.  **`cat` the file**: Start by reading the file:
    `cat q-shell-log-latency.log`
2.  **Filter by Method and Path (grep)**: Pipe to `grep` to find lines with the method _and_ path prefix. (Example: `GET` and `/api/catalog`):
    `| grep " GET /api/catalog"`
3.  **Filter by Cluster (grep)**: Add another `grep` for the cluster. (Example: `use1`):
    `| grep "cluster=use1"`
4.  **Filter by Status (grep)**: Add a `grep` for successful status codes. `status=2` will match `200`, `201`, etc.
    `| grep "status=2"`
5.  **Filter by Date/Time (awk)**: This is the hardest part. We pipe the remaining lines to `awk`.
    - `awk` splits each line into fields (columns) by spaces.
    - `$1` is the timestamp (e.g., `2024-04-17T14:23:11Z`).
    - We need to parse this timestamp to get the weekday and hour.
    - We can use `awk`'s `substr` function to get the hour and `system("date")` or `strftime` (if using `gawk`) to get the weekday.
    - A robust `awk` command (Example: filter for "Wednesday" between 13:00 and 17:59):
      `| awk -F'[T: ]' '{ \ hour = $2; \ cmd = "date -u -d " $1 " +%A"; \ cmd | getline weekday; \ close(cmd); \ if (weekday == "Wednesday" && hour >= 13 && hour < 18) { print $0 } \ }'`
      _Note: `date -d` syntax varies between GNU (Linux) and BSD (macOS). On macOS, you might need `date -u -jf %Y-%m-%d ...`._
6.  **Count Lines (wc)**: Finally, pipe the result to `wc -l` to count the lines.
    `| wc -l`

## 4. Shell Command (Example)

This single command pipeline combines the steps. **You must change the values in quotes** to match your specific question.

_(This example assumes Linux/GNU `date`. For macOS, the `date` command inside `awk` will be different.)_

```bash
# --- EXAMPLE COMMAND ---
# Replace all values (GET, /api/catalog, use1, Wednesday, 13, 18) with your question's values

cat q-shell-log-latency.log | \
  grep " GET /api/catalog" | \
  grep "cluster=use1" | \
  grep "status=2" | \
  awk -F'[T: ]' '{ \
    cmd = "date -u -d " $1 " +%A"; \
    cmd | getline weekday; \
    close(cmd); \
    hour = $2; \
    if (weekday == "Wednesday" && hour >= 13 && hour < 18) { print $0 } \
  }' | \
  wc -l
```

## 5. How to Run

1.  Save the log file to a directory.
2.  Open your terminal and `cd` to that directory.
3.  Copy, **edit**, and paste the shell command pipeline above.
4.  Press Enter. The command will output a single number.
5.  This number is your answer.
