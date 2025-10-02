# 9. Push an image to Docker Hub (1 Marks)

## 1. Problem Description

The task is to build a simple Docker image, tag it with a specific name derived from your email, and push it to a public repository on Docker Hub.

## 2. Understanding the Requirements

* **Platform**: Docker Hub.
* **Image Tag**: The image must have a tag that is the username part of your email. For `23f3004197@ds.study.iitm.ac.in`, the tag must be `23f3004197`.
* **Repository**: The Docker Hub repository must be public.
* **Submission**: The URL of your public repository on Docker Hub (e.g., `https://hub.docker.com/repository/docker/USER/REPO/general`).

## 3. Step-by-Step Solution

1. **Create a Docker Hub Account**:

      * If you don't have one, sign up for a free account at [hub.docker.com](https://hub.docker.com). Note your Docker Hub username.

2. **Create a Dockerfile**:

      * Create a new local folder for your project.
      * Inside the folder, create a file named `Dockerfile`.
      * Add the content for a very simple image, like one based on `alpine` that just prints a message. See the content below.

3. **Build the Docker Image**:

      * Open your terminal and navigate to the project folder.
      * Run the `docker build` command. Replace `<DOCKER_USER>` with your Docker Hub username and `<REPO_NAME>` with a name for your repository (e.g., `exam-image`).

    ```bash
    docker build -t <DOCKER_USER>/<REPO_NAME> .
    ```

      * Example: `docker build -t mynkpdr/hello-world .`

4. **Tag the Image**:

      * Now, add the required tag to the image you just built. The tag is `23f3004197`.

    ```bash
    docker tag <DOCKER_USER>/<REPO_NAME>:latest <DOCKER_USER>/<REPO_NAME>:23f3004197
    ```

      * Example: `docker tag mynkpdr/hello-world:latest mynkpdr/hello-world:23f3004197`

5. **Log in to Docker Hub**:

      * From your terminal, log in to your Docker Hub account.

    ```bash
    docker login
    ```

      * It will prompt for your username and password (or an access token).

6. **Push the Image to Docker Hub**:

      * Push the image with the specific tag to Docker Hub. This will automatically create the public repository if it doesn't exist.

    <!-- end list -->

    ```bash
    docker push <DOCKER_USER>/<REPO_NAME>:23f3004197
    ```

      * Example: `docker push mynkpdr/hello-world:23f3004197`
      * You can also push the `latest` tag if you wish: `docker push mynkpdr/hello-world:latest`

7. **Get the URL**:

      * Go to your Docker Hub account in the browser. You will see your new repository.
      * The URL will look like `https://hub.docker.com/r/<DOCKER_USER>/<REPO_NAME>` or `https://hub.docker.com/repository/docker/<DOCKER_USER>/<REPO_NAME>/general`. Copy this URL for submission.

## 4. Code / Configuration File (`Dockerfile`)

```dockerfile
# Use a minimal base image
FROM alpine:latest

# The command to run when the container starts
CMD ["echo", "Hello from my custom Docker image! This is for the exam."]
```

## 5. How to Run and Verify

1. After pushing, go to your repository on Docker Hub.
2. Under the "Tags" section, you should see the tag `23f3004197`.
3. Ensure the repository is public (this is the default).
4. The grader will use the Docker Hub API to query your repository and check for the existence of the required tag.

You can also verify by pulling the image on another machine:

```bash
docker pull <DOCKER_USER>/<REPO_NAME>:23f3004197
docker run <DOCKER_USER>/<REPO_NAME>:23f3004197
```

This should print the "Hello" message.
