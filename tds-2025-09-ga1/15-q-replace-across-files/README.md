# 15. Replace across files (0.8 Marks)

This guide shows two methods to replace `"IITM"` with `"IIT Madras"` in all files and calculate the SHA256 hash.

---

## Method 1: Using VS Code + WSL (Recommended for Beginners)

### Steps

1. **Unzip and Open Files**

   * Unzip the downloaded files into a new folder
   * Open this folder in **VS Code**

2. **Replace Text in VS Code**

   * Press `Ctrl + Shift + F` to open global search
   * Enable **Match Case** (Aa) to ensure accuracy
   * In the search box, type: `IITM`
   * In the replace box, type: `IIT Madras`
   * Click **Replace All**
   * Save all files (`Ctrl + K S`)

3. **Calculate Hash Using WSL**

   * Open terminal (`Ctrl + ~` in VS Code or system terminal)
   * If using Windows, enter WSL:

     ```powershell
     wsl -d Ubuntu
     ```

   * Navigate to your folder:

     ```bash
     cd path/to/your/folder
     ```

   * Run this command:

     ```bash
     cat * | sha256sum
     ```

   * Copy the **64-character hash** from the output.

---

## Method 2: Using `sed` in WSL/Linux (Command-Line Only)

This method directly replaces text inside all `.txt` files using `sed`.

### Steps

1. **Open WSL / Linux Terminal**

   ```powershell
   wsl -d Ubuntu
   ```

2. **Navigate to Your Folder**

   ```bash
   cd path/to/your/folder
   ```

3. **Run `sed` Replacement**

   * To replace `"IITM"` with `"IIT Madras"` in all `.txt` files:

     ```bash
     sed -i 's/IITM/IIT Madras/gI' *.txt
     ```

     **Explanation:**

     * `-i` → edit files in-place
     * `s/.../.../gI` → substitute all occurrences, case-insensitive (`I`)
     * `*.txt` → apply to all text files

4. **Verify Replacement**

   ```bash
   grep -R "IITM" .
   ```

   (If nothing shows, all replacements are done.)

5. **Calculate Hash**

   ```bash
   cat *.txt | sha256sum
   ```

---

## Important Notes

* Always **save files** before running hash commands
* The replacement is **case-insensitive** (`gI`)
* Hash output will be a **64-character hexadecimal string**
* Use quotes if your path has spaces:

  ```bash
  cd "My Folder Name"
  ```
