# 6. Submit a Jules-Generated Pull Request (1 Mark)

## 1. Problem Description

This task involves using Google's AI coding assistant, **Jules ([https://jules.google.com/](https://jules.google.com/))**, to author code changes in a personal GitHub repository and open a pull request (PR). The PR must contain a unique verification number for grading purposes.

## 2. Understanding the Requirements

* **Tool**: Jules AI (browser version at `jules.google.com`, though CLI just released)
* **Action**: Generate a pull request against one of your personal, public GitHub repositories.
* **Verification**: The title or the body of the pull request must include a specific, randomly generated number provided by the exam platform.
* **Submission**: The final public URL of the GitHub pull request.

## 3. Step-by-Step Solution

1. **Create a GitHub Repository**

   * Log in to your GitHub account.
   * Create a new **public** repository (e.g., `jules-test-repo`).
   * Initialize it with a `README.md` file so Jules has something to work with.

2. **Open Jules in the Browser**

   * Go to **[https://jules.google.com/](https://jules.google.com/)**
   * Sign in with your Google account.
   * Connect your GitHub account when prompted (Jules will request authorization). You can give access to all repositories or only specific ones.
   * Once connected, select your repository (`jules-test-repo`) from the dashboard.

3. **Give Jules a Task (Browser Prompt)**

   * From the Jules UI, open the repository workspace.
   * In the chat input, give a task like :

     ```bash
     Create a new file named 'main.py' with a Python function called 'add' that takes two arguments and returns their sum.

     Open a pull request for these changes.
     Title: feat: add basic calculator [YOUR_VERIFICATION_NUMBER]
     Body: Jules-generated PR. Verification number: [YOUR_VERIFICATION_NUMBER]
     ```

     (replace `[YOUR_VERIFICATION_NUMBER]` with your actual number)

   * Jules will draft the change and show you the diff before applying it.

4. **Approve and Let Jules Apply the Changes**

   * After that, Jules will prepare the PR with the title and description. Click the tiny button and select `Publish PR`.

5. **Get the PR URL**

   * After creation, Jules will give you the GitHub PR link.
   * You can also find it manually under the "Pull requests" tab on GitHub.
   * Copy the URL (e.g., `https://github.com/<USER>/jules-test-repo/pull/1`).

6. **Submit the URL**

   * Paste the URL into the exam submission box.
   * Make sure the repo is public and the PR stays open until graded.

## 4. How to Verify

1. **Check the PR URL**: Open it publicly in a browser.
2. **Verify Commit Author**: Look in the "Commits" tab, the author should show as Jules (e.g., `google-labs-jules`).
3. **Check the Verification Number**: Confirm the unique number is clearly shown in the PR's title or body.
4. If these are all correct, you're ready to submit.
