# 11. Ship a Jules-Authored Test Workflow (2 Marks)

## 1. Problem Description

This is an advanced task similar to Q6 that requires you to use Google's AI coding assistant, **Jules (via the browser at [https://jules.google.com/](https://jules.google.com/))**, to perform a complete end-to-end development cycle. You must instruct Jules to write a Python function, create a corresponding test suite using `pytest`, and set up a GitHub Actions workflow to run those tests automatically. The final submission is a pull request (PR) created by Jules that has a successful ("green") continuous integration (CI) check.

## 2. Understanding the Requirements

- **Tool**: Jules AI (`jules.google.com` in browser)
- **Task**: Jules must generate three distinct components based on a detailed coding brief:

  1. A Python module (`streak.py`) with a specific function.
  2. A test file (`tests/test_streak.py`) with `pytest` test cases.
  3. A GitHub Actions configuration file (`.github/workflows/pytest.yml`).

- **Verification**: The submitted pull request will be checked for several conditions:

  - Authored by Jules.
  - Contains the unique verification number provided by the exam platform.
  - Has a successful GitHub Actions run.
  - The successful run contains a successful `pytest` step.

- **Submission**: The final public URL of the GitHub pull request.

## 3. Step-by-Step Solution

### Step 1: Set Up the GitHub Repository

1. Create a new **public** GitHub repository. Example: `jules-streak-finder`.
2. Initialize it with a `README.md`.
3. In the repository settings, under **Actions > General**, ensure **"Allow all actions and reusable workflows"** is selected.

### Step 2: Prepare the Project Environment (Directly in GitHub)

1. In your repository on GitHub, click **Add file > Create new file**.
2. Name the file `requirements.txt`.
3. Add `pytest` as the content:

   ```
   pytest
   ```

4. Scroll down and **commit directly to the main branch**.

### Step 3: Provide the Detailed Brief to Jules

1. Open [Jules in the browser](https://jules.google.com/) and navigate to your repository workspace.
2. Paste the **entire coding brief** from the question in one message to Jules. Add the following (replace `[YOUR_VERIFICATION_NUMBER]` with your actual number):

   ```plaintext
   Open a pull request for these changes.
   Title: feat: added streak files [YOUR_VERIFICATION_NUMBER]
   Body: Jules-generated PR. Verification number: [YOUR_VERIFICATION_NUMBER]
   ```

3. Jules will read it, create a plan, and generate the code, committing it to a new branch.

### Step 4: Review Jules' Plan and Code

1. Approve the proposed plan.
2. Jules will generate:

   - `streak.py`
   - `tests/test_streak.py`
   - `.github/workflows/pytest.yml`

### Step 5: Create the Pull Request

1. After that, Jules will prepare the PR with the title and description. Click the tiny button and select `Publish PR`.

   ![Publish PR](https://i.imgur.com/mKdnGcs.png)

2. If you get the above, then Jules will create the PR in your repository.

### Step 6: Wait for GitHub Actions to Succeed

1. On the PR page, observe the CI check (GitHub Actions) running.
2. Wait until the workflow finishes with a **green checkmark**. This ensures the tests (`pytest`) ran successfully.

    ![Success Check](https://i.imgur.com/MqEnJNy.png)
3. If you don't see a green checkmark, click on "Details" to investigate the CI logs and rerun the steps.

### Step 7: Submit the URL

1. Copy the PR URL from GitHub.
2. Paste it as your final answer. Keep the PR public and open until graded.

---

## 4. Code / Configuration File (Full Prompt for Jules)

Paste this **entire block** into the Jules chat box (Might be different for your question):

```python
Create streak.py with a function longest_positive_streak(nums: list[int]) -> int.

Rules:
- Return the length of the longest run of consecutive values strictly greater than 0.
- An empty list returns 0.
- Non-positive numbers break the streak (0 or negatives reset the count).
- The function must be deterministic and pure: no randomness, prints, or global state.

Example:
- longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3
- longest_positive_streak([]) == 0
- longest_positive_streak([1, 1, 1]) == 3

Add tests/test_streak.py with pytest tests that cover at least:
- Empty input
- Data with multiple streaks (ensure the longest wins)
- Inputs containing zeros and negatives.

Add a GitHub Actions workflow (.github/workflows/pytest.yml) that runs pytest on every push and pull_request.
```

---

## 5. How to Verify

1. **Check the PR URL**: Open it in a browser.
2. **Verify Jules' Commits**: The author should be `google-labs-jules`.
3. **Confirm Verification Number**: Ensure it appears in the PR title or body.
4. **Confirm Successful CI**: The PR must show a green checkmark; click "Details" to ensure the `pytest` step passed.
5. If all these are correct, the submission is valid.
