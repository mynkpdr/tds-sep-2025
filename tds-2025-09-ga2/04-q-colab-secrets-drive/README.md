# 4. Harden a Colab secrets + Drive workflow (0.75 Marks)

## 1. Problem Description

This task involves using Google Colab to process a CSV file of incident metrics stored in Google Drive. You need to securely access a secret API key, mount Google Drive, read the data, perform a calculation, and produce a specific verification code. The provided Python script contains bugs that must be fixed.

## 2. Understanding the Requirements

Based on the email (`23f3004197@ds.study.iitm.ac.in`), the following values are required:

* **Secret Name**: `GA2_API_KEY`
* **Secret Value**: `GA2-0B64D338`
* **Expected Verification Code**: `D338-1451`

The process involves:

1. Uploading a provided CSV file to a specific path in your Google Drive.
2. Creating a secret in Google Colab with the specified name and value.
3. Fixing a Python script to correctly mount Drive, access the secret, and perform the calculation.
4. The calculation is to sum the `failures` for all time windows where the `error_rate` (failures / requests) is `≥ 0.02`.
5. The final code should be the last four characters of the API token, a hyphen, and the zero-padded sum of failures.

## 3. Step-by-Step Solution

1. **Prepare Google Drive**:

      * Download the `q-colab-secrets-drive.csv` file from the exam page.
      * In your Google Drive, create a folder named `ga2-deployment`.
      * Upload the downloaded CSV file into this folder and rename it to `incident-metrics.csv`. The final path should be `MyDrive/ga2-deployment/incident-metrics.csv`.

2. **Set up Google Colab**:

      * Open a new Colab notebook at [colab.research.google.com](https://colab.research.google.com).
      * Click the "key" icon on the left sidebar to open "Secrets".
      * Click "+ Add a new secret".
      * Set the **Name** to `GA2_API_KEY`.
      * Set the **Value** to `GA2-08F23A9D`.
      * Ensure "Notebook access" is toggled on.

3. **Fix the Python Script**:

      * The original script has several bugs:
          * The Drive mount path is wrong (`/content/gdrive` vs `/content/drive`).
          * The secret lookup is incorrect (`userdata["GA2_API_KEY"]` vs `userdata.get("GA2_API_KEY")`).
          * The path to the CSV is slightly off in the example (`/content/drive/MyDrive/...` vs `/content/gdrive/MyDrive/...`).
          * The final string formatting logic is incorrect (`api_token[:4]` vs `api_token[-4:]` and doesn't handle padding).
      * Copy the corrected Python code from the section below into a Colab cell.

4. **Run and Get the Code**:

      * Execute the Colab cell.
      * It will first ask for permission to mount your Google Drive. Follow the authentication flow.
      * Once executed, the notebook will print the verification code. It should be `D338-1451`.
      * Submit this code to the exam platform.

## 4. Corrected Python Code (for Colab)

```python
from google.colab import drive, userdata
import pandas as pd
from pathlib import Path

# 1. Mount Google Drive at the correct path
drive.mount("/content/drive")

# 2. Get the secret using the correct method
api_token = userdata.get("GA2_API_KEY")

# 3. Define the correct root path for the CSV file
root = Path("/content/drive/MyDrive/ga2-deployment")
data = pd.read_csv(root / "incident-metrics.csv")

# Calculate error_rate per window
error_rate = data["failures"] / data["requests"]

# Filter for windows with error rate >= 0.02
critical = data[error_rate >= 0.02]

# 4. Calculate the sum of failures for critical windows
total_failures = critical['failures'].sum()

# 5. Format the verification code correctly
# Use the last 4 characters of the token and zero-pad the total to 3 digits
verification = f"{api_token[-4:].upper()}-{total_failures:03d}"

print(verification)
```

## 5. How to Run and Verify

Running the corrected Python code in the configured Colab environment is the verification step itself. The output `D338-1451` is the answer to be submitted.
