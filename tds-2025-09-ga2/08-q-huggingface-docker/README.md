# 8. Publish a Docker Space with environment guardrails (1 marks)

## 1. Problem Description

This task requires you to create and configure a Hugging Face Space using the Docker SDK. The Space must be configured with a specific name, port, secret, and other metadata. You will need to provide a `Dockerfile`, `README.md`, and `requirements.txt`.

## 2. Understanding the Requirements

Based on the email (`23f3004197@ds.study.iitm.ac.in`), you must use the following specific values:

* **Space Name & Title**: `ga2-187e43`
* **Application Port (`app_port`)**: `7423`
* **Secret Name**: `GA2_TOKEN_624F`
* **README Description Token**: `deployment-ready-ga2-187e43`

Your setup must include:

* A public Hugging Face Space using the **Docker SDK** on the **CPU Basic** tier.
* A `README.md` file with `sdk: docker` and `app_port: 7423` in its frontmatter.
* A `Dockerfile` that:
  * Uses a `python:3.11-slim` base image.
  * Creates a non-root user with UID 1000.
  * Sets an `APP_PORT` environment variable and exposes the correct port (`7423`).
  * Runs a `uvicorn` server for a FastAPI app.
* A `requirements.txt` file with `fastapi` and `uvicorn`.
* A secret named `GA2_TOKEN_624F` created in the Space settings.

## 3. Step-by-Step Solution

1. **Create the Hugging Face Space**:

      * Go to [huggingface.co/new-space](https://huggingface.co/new-space).
      * Set the **Space name** to `ga2-187e43`.
      * Select **Docker** as the SDK.
      * Choose the **CPU basic** hardware.
      * Ensure it's **Public**.
      * Click "Create Space".

2. **Clone the Repository Locally**:

      * On the Space page, find the "Files and versions" tab and use the `git clone` command to clone the repository to your local machine.

3. **Create Project Files**:

      * In the cloned repository, create the four required files: `README.md`, `Dockerfile`, `requirements.txt`, and a simple `main.py` for the FastAPI app. Populate them with the content from the section below.

4. **Push Files to Hugging Face**:

      * Commit and push your changes to the Hugging Face repository.

    <!-- end list -->

    ```bash
    git add .
    git commit -m "feat: initial docker space setup"
    git push
    ```

5. **Configure the Secret**:

      * On your Space page on Hugging Face, go to the "Settings" tab.
      * Scroll down to "Variables and Secrets".
      * Click "New secret".
      * Enter `GA2_TOKEN_624F` as the **Name**.
      * Enter any value for the secret (e.g., `my-secret-token`). The value doesn't matter, only the name.

6. **Verify the Build**:

      * Go back to the "App" or "Logs" tab of your Space. Hugging Face will automatically start building the Docker image.
      * Wait for the build to complete and the application to be running. If it works, you'll see a message like "Application is running."

7. **Submit the URL**:

      * Copy the public URL of your space (e.g., `https://huggingface.co/spaces/YOUR_USERNAME/ga2-187e43`) and submit it.

## 4. Code / Configuration Files

#### `README.md`

```yaml
---
title: ga2-187e43 
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7423
---

This Space demonstrates a containerized FastAPI app deployed with the Docker SDK on Hugging Face Spaces. deployment-ready-ga2-187e43
It listens on port **7423** (configured via app_port) and expects a secret named `GA2_TOKEN_624F` to be set in the Space settings.
```

#### `Dockerfile`

```dockerfile
# Use a slim Python base image
FROM python:3.11-slim

# Create a non-root user with UID 1000
RUN useradd -m -u 1000 user

# Set the working directory
WORKDIR /home/user/app

# Copy requirements and install dependencies as the root user first
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY --chown=user . .

# Switch to the non-root user
USER user

# Set environment variable for the port and expose it
ARG APP_PORT=7423
ENV APP_PORT=${APP_PORT}
EXPOSE 7423

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7423"]
```

#### `requirements.txt`

```
fastapi
uvicorn[standard]
```

#### `main.py`

```python
from fastapi import FastAPI, HTTPException
import os

app = FastAPI()

TOKEN = os.environ.get("GA2_TOKEN_624F", None)


@app.get("/")
def read_root():
    port = os.getenv("APP_PORT", "N/A")
    return {"message": f"Hello from Hugging Face Docker Space on port {port}!"}


@app.get("/token")
def token():
    if TOKEN:
        return {"success": True, "token": TOKEN[:4]}
    else:
        raise HTTPException(status_code=404, detail="Token not found")

```

## 5. How to Run and Verify

The build process on Hugging Face is the primary verification. The grader will check your Space's configuration via the Hugging Face API, verifying:

* The SDK is Docker.
* The `app_port` and `title` in the `README.md` frontmatter are correct.
* The `Dockerfile` contains the required commands (e.g., `USER user`, `EXPOSE 7423`).
* The `requirements.txt` includes FastAPI.
* The secret `GA2_TOKEN_624F` exists.
