# 4. Run command with npx (0.2 Marks)

## **Step 1: Install Node.js (includes npm and npx)**

### **Windows**

1. Go to [Node.js Download Page](https://nodejs.org/en/download/).
2. Download the **LTS version** (recommended for stability).
3. Run the installer and follow the prompts:

   * Keep default settings.
   * Ensure **“Add to PATH”** is checked.
4. Open **Command Prompt** or **PowerShell** and check installation:

```bash
node -v
npm -v
npx -v
```

You should see version numbers for **Node**, **npm**, and **npx**.

---

### **macOS**

1. Go to [Node.js Download Page](https://nodejs.org/en/download/) and download the **macOS Installer**.
2. Open the `.pkg` file and follow the instructions.
3. Open Terminal and check:

```bash
node -v
npm -v
npx -v
```

---

### **Linux (Ubuntu/Debian)**

```bash
sudo apt update
sudo apt install nodejs npm -y
node -v
npm -v
npx -v
```

> Note: `npx` comes bundled with **npm 5.2+**. If your npm version is older, upgrade:

```bash
sudo npm install -g npm
```

---

## **Step 2: Navigate to the folder with `README.md`**

```bash
cd /path/to/directory
```

> Replace `/path/to/directory` with the actual folder containing `README.md`.

---

## **Step 3: Run Prettier with npx**

Use npx to run Prettier **without installing it globally**:

```bash
npx -y prettier@3.4.2 README.md | sha256sum
```

**Explanation:**

1. `npx -y prettier@3.4.2 README.md`

   * Runs **Prettier version 3.4.2** on the file.
   * `-y` auto-confirms the temporary installation if needed.
2. `| sha256sum`

   * Pipes the formatted output into `sha256sum` to generate a unique hash.

---

## **Step 4: Copy the output**

* Terminal will return something like:

```
7c4924c22fca725f7c2214333b4d0fd7df5dd7682d5f6f99aa81e8b648f2d877  -
```

* That **hexadecimal string** is the SHA-256 checksum of your formatted `README.md`.

---

## **Step 5: Paste the output**

* Copy the **entire line** exactly as shown in the terminal.
* This confirms that Prettier ran successfully and your file formatting is verified.

---

If you want, I can also **give the expected SHA-256 hash format** for a standard `README.md` template so you’ll know what it should look like before running it.

Do you want me to do that?
