# 8. Create a Scheduled GitHub Action (1 Marks)

## 1. Problem Description

The task is to create a GitHub Action workflow that runs on a daily schedule, performs a small change in the repository (like updating a file with the current timestamp), and commits that change back to the repository. The workflow must also include a step that references your email address in its name.

This project simulates a DevOps task for "DevSync Solutions," a company that wants to automate daily repository activity for tracking and documentation purposes.

## 2. Understanding the Requirements

- **Platform**: GitHub Actions.
- **Trigger**: The workflow must be triggered by a `schedule` event using `cron` syntax for a daily run.
- **Actions**: The workflow must:
  1. Check out the repository's code.
  2. Run a step that updates a file (e.g., `last_updated.txt`).
  3. Contain a step where the `name` includes your email: `23f3004197@ds.study.iitm.ac.in`.
  4. Commit the changed file back to the repository.
- **Repository Setup**: You need a GitHub repository to host the workflow file.
- **Output**: A public GitHub repository URL where the scheduled action has successfully run.

## 3. Step-by-Step Solution

### Step 1: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and create a new public repository (e.g., `daily-commit-action`).
2. Initialize it with a `README.md` file.

### Step 2: Create the Workflow File

1. In your new repository, navigate to the **Actions** tab. GitHub might suggest a simple workflow; you can skip that and set one up yourself.
2. Click on the "set up a workflow yourself" link.
3. This will create a new file. Name it `daily_commit.yml` (or keep `main.yml`). The full path must be `.github/workflows/daily_commit.yml`.
4. Paste the YAML code provided below into this file.

### Step 3: Understand and Customize the Workflow Code

The YAML file defines the workflow's triggers and jobs.

- **`name`**: A descriptive name for the workflow.
- **`on`**: Defines the triggers.
  - **`schedule`**: We use a `cron` job to run daily. `0 5 * * *` means it runs at 5:00 AM UTC every day. You can customize this.
  - **`workflow_dispatch`**: This allows you to run the workflow manually from the Actions tab, which is essential for testing.
- **`jobs`**: Contains the sequence of tasks.
  - **`runs-on`**: Specifies the runner environment (e.g., `ubuntu-latest`).
  - **`steps`**: A list of individual actions.
    - `actions/checkout@v4`: A standard action to check out your repository's code so the workflow can access it.
    - **Update File**: A `run` step that uses shell commands to write the current date into a file named `last_updated.txt`. This is the step where we add the required email to the `name`.
    - **Commit and Push**: A `run` step that configures Git, adds the changed file, commits it with a message, and pushes it back to the repository.

## 4. Code (`.github/workflows/daily_commit.yml`)

```yaml
name: Daily Repository Update

on:
  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

  # Runs at 05:00 UTC every day
  schedule:
    - cron: "0 5 * * *"

jobs:
  update-and-commit:
    runs-on: ubuntu-latest

    steps:
      # Step 1: Check out the repository code
      - name: Checkout repository
        uses: actions/checkout@v4

      # Step 2: Update a file with the current date
      # The name of this step includes the required email address
      - name: Update last_updated.txt with current date - 23f3004197@ds.study.iitm.ac.in
        run: |
          echo "Last updated on: $(date -u)" > last_updated.txt

      # Step 3: Commit and push the changes
      - name: Commit and push
        run: |
          # Configure git with bot user
          git config --global user.name 'github-actions[bot]'
          git config --global user.email 'github-actions[bot]@users.noreply.github.com'

          # Add changes to staging, commit, and push
          git add last_updated.txt

          # Commit changes
          git commit -m "Automated update of last_updated.txt"

          # Push the changes
          git push
```

## 5. How to Verify

1. **Commit the File**: After pasting the code into `.github/workflows/daily_commit.yml`, commit the file to your `main` branch.
2. **Manual Trigger**:
   - Go to the **Actions** tab in your repository.
   - In the left sidebar, click on "Daily Repository Update".
   - You will see a message: "This workflow has a `workflow_dispatch` event trigger."
   - Click the **Run workflow** button to trigger it manually for testing.
3. **Check the Run**:
   - Click on the running workflow to see its progress.
   - Wait for all steps to complete successfully (they should all have green checkmarks).
   - Once finished, go back to the **Code** tab of your repository.
4. **Confirm the Commit**:
   - You should see a new file named `last_updated.txt`.
   - Check the repository's commit history. You should see a new commit with the message "Automated update of last_updated.txt" authored by "github-actions[bot]".
5. **Submit URL**: The URL of your repository (e.g., `https://github.com/your-username/daily-commit-action`) is the answer to submit.
