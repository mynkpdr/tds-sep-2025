# 6. Create a GitHub Action (1 Marks)

## 1. Problem Description

The task is to create a basic GitHub Action in one of your repositories. The action must have a step whose name contains your specific email address, `23f3004197@ds.study.iitm.ac.in`. You need to trigger the action and then submit the repository URL for verification.

## 2. Understanding the Requirements

* **Platform**: GitHub Actions.
* **Repository**: Any public GitHub repository you own.
* **Workflow Step**: One of the steps in the workflow file must have a `name` field that includes the string `23f3004197@ds.study.iitm.ac.in`.
* **Execution**: The action must be the most recent run in the repository.
* **Submission**: The URL of the GitHub repository (e.g., `https://github.com/USER/REPO`).

## 3. Step-by-Step Solution

1. **Choose or Create a Repository**:

      * You can use an existing public repository or create a new one on GitHub. Let's call it `github-action-test`.

2. **Create the Workflow Directory**:

      * In your repository, you need to create a `.github/workflows` directory. GitHub Actions are defined by YAML files placed in this directory.

3. **Create the Workflow File**:

      * Inside `.github/workflows`, create a new file named `main.yml` (or any other `.yml` name).
      * Add the YAML content provided below to this file. This workflow is simple: it triggers on a push to the `main` branch and has a single job with one step that prints a message. The crucial part is the `name` of that step.

4. **Commit and Push the Workflow**:

      * Commit the `main.yml` file to your repository and push it to the `main` branch on GitHub.

    ```bash
    # On your local machine, in the repo folder
    git add .github/workflows/main.yml
    git commit -m "feat: add simple github action"
    git push origin main
    ```

5. **Verify the Action Run**:

      * Go to your repository on GitHub and click the "Actions" tab.
      * You will see your workflow running or completed. This push automatically triggered it.
      * Click on the workflow run to see the details and confirm that the step named with your email executed successfully.

6. **Submit the Repository URL**:

      * Copy the URL of your repository (e.g., `https://github.com/YOUR_USERNAME/github-action-test`) and submit it to the exam platform.

## 4. Code / Configuration File (`.github/workflows/main.yml`)

```yaml
# A simple workflow to demonstrate a custom step name.
name: CI

# Controls when the workflow will run
on:
  # Triggers the workflow on push events but only for the "main" branch
  push:
    branches: [ "main" ]
  
  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # A step with a name containing the required email address
      - name: "Verification step for 23f3004197@ds.study.iitm.ac.in"
        run: echo "This step is being checked by the grader!"

      - name: A second step
        run: echo "Hello, world!"
```

## 5. How to Run and Verify

The action runs automatically when you push the workflow file to your `main` branch. To verify:

1. Go to the "Actions" tab of your repository on GitHub.
2. Ensure that the latest workflow run was successful (has a green checkmark).
3. Click into the run, then the `build` job, and you should see the step named `"Verification step for 23f3004197@ds.study.iitm.ac.in"` in the log.
    The exam's automated grader will use the GitHub API to check your repository's most recent action run for a step with the required name.
