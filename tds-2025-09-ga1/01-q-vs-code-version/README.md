# 1. VS Code Version (0.2 Marks)

## **Step 1: Install Visual Studio Code**

### **Windows**

1. Go to [VS Code Download Page](https://code.visualstudio.com/Download).
2. Download the **Windows installer** (User or System Installer).
3. Run the installer and **follow the prompts**:

   * Check **“Add to PATH”** (important for running `code` from the terminal).
   * You can also check **“Add Open with Code action”** for right-click context menu.
4. Finish installation.

### **macOS**

1. Go to [VS Code Download Page](https://code.visualstudio.com/Download).
2. Download the **macOS Universal** zip.
3. Open the zip and **drag Visual Studio Code to Applications folder**.
4. Open VS Code, then press `Cmd + Shift + P` → type **“Shell Command: Install 'code' command in PATH”** → press Enter.

### **Linux**

* For **Debian/Ubuntu**:

```bash
sudo apt update
sudo apt install software-properties-common apt-transport-https wget
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
sudo apt update
sudo apt install code
```

---

## **Step 2: Open VS Code and Install Command Line Tool**

* Open VS Code.
* Press:

  * **Windows/Linux:** `Ctrl + Shift + P`
  * **Mac:** `Cmd + Shift + P`
* Type **“Shell Command: Install 'code' command in PATH”** → Enter.
* Close and reopen your terminal.

---

## **Step 3: Run `code -s`**

1. Open your **Terminal** or **Command Prompt**.

   * Windows: `Win + R` → type `cmd` → Enter
   * macOS: Spotlight → Terminal → Enter
   * Linux: Open terminal

2. Type:

```bash
code -s
```

3. Press **Enter**.

---

## **Step 4: Understand the output**

* If **VS Code is installed correctly** and `code` command works, you’ll see something like:

```
--status        Print process and workspace information.
--version       Print VS Code version.
--help          Print usage information.
--list-extensions List installed extensions.
--install-extension <ext> Install an extension.
--uninstall-extension <ext> Uninstall an extension.
```

* If **it fails**, you’ll see:

```
'code' is not recognized as an internal or external command
```

→ This means the command-line tool is not in your PATH. Repeat **Step 2**.

---

## ✅ **Step 5: Success Check**

* What is the output of code -s?

```bash
Version:          Code 1.104.1 (0f0d87fa9e96c856c5212fc86db137ac0d783365, 2025-09-17T23:36:24.973Z)
OS Version:       Windows_NT x64 10.0.19045
CPUs:             AMD Ryzen 9 9950X3D with Radeon Graphics          (16 x 5.7 GHz)
Memory (System):  29.16GB (14.19GB free)
............
............
............
............
............
............
```
