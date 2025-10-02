# 10. Configure a Codespace devcontainer (0.75 Marks)

## 1. Problem Description

The task is to configure a development environment for a public GitHub repository using a `devcontainer.json` file. This configuration should set up a GitHub Codespace with a specific name, pre-installed Python tools, and VS Code extensions.

## 2. Understanding the Requirements

Based on the email (`23f3004197@ds.study.iitm.ac.in`), the following values are required:

* **Devcontainer Name**: `ga2-aa28c9`

The `.devcontainer/devcontainer.json` file must specify:

* The exact name `ga2-aa28c9`.
* The `ghcr.io/devcontainers/features/python:1` feature.
* The VS Code extensions `astral-sh.uv` and `ms-python.python`.
* A `postCreateCommand` that uses `uv` to install `fastapi`.

You need to launch a Codespace from this configuration and submit the repository slug (`OWNER/REPO`) and a temporary `GITHUB_TOKEN` from within the Codespace terminal.

## 3. Step-by-Step Solution

1. **Create a Public GitHub Repository**:

      * Create a new public repository on GitHub, for example, `codespace-devcontainer-demo`.

2. **Create the Devcontainer Configuration**:

      * In your local clone of the repository, create a directory named `.devcontainer`.
      * Inside this directory, create a file named `devcontainer.json`.
      * Copy the devcontainer JSON content from the section below into this file.

3. **Commit and Push the Configuration**:

      * Commit the `.devcontainer/devcontainer.json` file and push it to your repository on GitHub.

    ```bash
    git add .devcontainer/devcontainer.json
    git commit -m "feat: add devcontainer configuration"
    git push origin main
    ```

4. **Launch the Codespace**:

      * Go to your repository on GitHub.
      * Click the green "\<\> Code" button.
      * Select the "Codespaces" tab.
      * Click "Create codespace on main".
      * Wait for GitHub to build and launch your Codespace. This might take a few minutes as it sets up the container, runs the `postCreateCommand`, and installs extensions.

5. **Get the Repository and Token**:

      * Once the Codespace is running (you'll see a VS Code interface in your browser), open a new Terminal (`Ctrl+` `` ` ``).
      * In the terminal, run the following command:

    <!-- end list -->

    ```bash
    echo $GITHUB_REPOSITORY $GITHUB_TOKEN
    ```

      * This will print the repository slug and a temporary GitHub Personal Access Token (PAT) that is valid for the session.
      * The output will look something like this: `YOUR_USERNAME/codespace-devcontainer-demo ghp_...`

6. **Submit the Credentials**:

      * Copy the entire line of output (both the slug and the token, separated by a space) and paste it into the answer field on the exam page.

## 4. Code / Configuration File (`.devcontainer/devcontainer.json`)

```json
{
  // The name for the devcontainer, as required by the exam.
  "name": "ga2-aa28c9",

  // Use a base image. The Universal Image is a good default.
  "image": "mcr.microsoft.com/devcontainers/universal:2",

  "features": {
    // Install Python using the devcontainer feature.
    "ghcr.io/devcontainers/features/python:1": {}
  },

  "customizations": {
    "vscode": {
      // Install required VS Code extensions.
      "extensions": [
        "astral-sh.uv",
        "ms-python.python"
      ]
    }
  },

  // A command to run after the container is created.
  "postCreateCommand": "uv pip install fastapi"
}
```

## 5. How to Run and Verify

The primary verification is done by the exam platform after you submit the repository slug and token. The grader will use the provided token to access the GitHub API and:

1. Verify it can access the specified repository.
2. Check for the existence and content of the `.devcontainer/devcontainer.json` file.
3. Confirm that all the required keys and values (name, features, extensions, command) are present and correct in the JSON file.
4. Check that there is an active Codespace for the repository.

Make sure to **keep your Codespace running** while you submit the answer, as the grader may check its state.
