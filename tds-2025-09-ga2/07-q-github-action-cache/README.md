# 7. Create a GitHub Action with dependency caching (1 Marks)

## 1. Problem Description

This task requires you to create a GitHub Actions workflow that utilizes `actions/cache@v4` (or newer) to cache dependencies. The workflow must use a specific cache key and include a step with a specific name to signal that the cache has been primed.

## 2. Understanding the Requirements

Based on the email (`23f3004197@ds.study.iitm.ac.in`), the following specific values must be used:

* **Cache Key**: `cache-7845754`
* **Step Name**: `prime-cache-7845754`

The workflow must:

* Use the `actions/cache@v4` action.
* Attempt to restore a cache with the key `cache-7845754`.
* Include a step explicitly named `prime-cache-7845754`.
* This step must succeed.
* You must run the workflow at least once.
* Submit the repository URL for verification.

## 3. Step-by-Step Solution

1. **Choose or Create a Repository**:

      * Use any public GitHub repository. Let's create one named `action-caching-demo`.

      > **Note:** You may need to create a separate github repository for this question or combine Q6 and Q7 because it looks for the most recent action which may interfere with the previous question.

2. **Create the Workflow File**:

      * In the repository, create the directory structure `.github/workflows`.
      * Inside, create a file named `caching.yml`.
      * Add the YAML content provided below. This workflow demonstrates caching for Python dependencies installed with `uv`.

3. **Understand the Workflow Logic**:

      * **Cache Step**: The `actions/cache@v4` step uses the exact key `cache-7845754`. It caches the `~/.cache/uv` directory. It also has an `id` (`cache-uv`) so we can check if the cache was hit.
      * **Install Dependencies**: This step runs `uv pip install` to install dependencies from a `requirements.txt` file. If the cache was hit, this step will be much faster.
      * **Priming Step**: The step named `prime-cache-7845754` is crucial. It checks the output of the cache step (`steps.cache-uv.outputs.cache-hit`) and prints a message. The important thing is that this step exists and succeeds.

4. **Create `requirements.txt`**:

      * For the example to work, create a `requirements.txt` file in the root of your repository with some Python packages.

5. **Commit and Push**:

      * Commit both `caching.yml` and `requirements.txt` and push to GitHub.

    ```bash
    git add .github/workflows/caching.yml requirements.txt
    git commit -m "feat: add workflow with dependency caching"
    git push origin main
    ```

6. **Run the Workflow**:

      * Pushing the commit will trigger the workflow. Go to the "Actions" tab in your repository to monitor its progress.
      * The first time it runs, it will be a "cache miss". The dependencies will be downloaded and the cache will be saved at the end of the job.
      * You can re-run the job to see a "cache hit", but for this problem, a single successful run is sufficient.

## 4. Code / Configuration Files

#### `.github/workflows/caching.yml`

```yaml
name: CI with Caching

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  build-with-cache:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up uv
        uses: astral-sh/setup-uv@v5
      
      - name: Create virtual environment
        run: uv venv

      - name: Cache uv dependencies
        uses: actions/cache@v4
        id: cache-uv # Give the step an id to check its output
        with:
          path: ~/.cache/uv
          key: cache-7845754

      - name: Install dependencies
        run: uv pip install -r requirements.txt

      - name: prime-cache-7845754
        run: |
          if [[ "${{ steps.cache-uv.outputs.cache-hit }}" == "true" ]]; then
            echo "Cache hit! Dependencies were restored."
          else
            echo "Cache miss. Dependencies were installed and cache will be saved."
          fi
```

#### `requirements.txt`

```
pandas
numpy
fastapi
```

## 5. How to Run and Verify

1. After pushing the files, go to the "Actions" tab of your repository.
2. Ensure the "CI with Caching" workflow has completed successfully.
3. The grader will inspect this latest run, checking for:
      * The use of `actions/cache@v4`.
      * The presence of the exact cache key `cache-7845754` in the workflow file.
      * A successful step named `prime-cache-7845754`.
4. Submit the repository URL.
