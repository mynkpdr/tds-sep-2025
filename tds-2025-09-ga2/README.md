# Summary of all the questions

### **Question 1: Author a deployment architecture markdown**

* **What it Covered:** Writing technical documentation using **GitHub Flavored Markdown (GFM)**. This included creating headings, tables, GFM task lists, and an architecture diagram using **Mermaid**.

* **Why you need it:** Clear communication is the most critical non-technical skill. Documenting your software's architecture and deployment plans ensures your entire team is aligned. Mermaid allows you to create and version diagrams as code, directly within your documentation, making it easy to keep visuals up-to-date. This is a fundamental skill for planning, collaboration, and knowledge sharing.

### **Question 2: Compress an image**

* **What it Covered:** Performing **lossless image compression**, reducing a PNG's file size to under 400 bytes by converting it to a modern format like WebP without altering pixel data.

* **Why you need it:** Website and application performance. Large images are a primary cause of slow load times, leading to a poor user experience and higher bandwidth costs. Knowing how to optimize web assets is a crucial skill for front-end developers, UI/UX designers, and anyone building user-facing products.

### **Question 3: Host your portfolio on GitHub Pages**

* **What it Covered:** Deploying a simple static HTML website using **GitHub Pages**, a free hosting service integrated into GitHub.

* **Why you need it:** This is the fastest and most common way for developers to create a public portfolio, host documentation for a project, or launch a simple landing page. It demonstrates a foundational understanding of Git, web hosting, and how to make your work accessible to the world.

### **Question 4: Harden a Colab secrets + Drive workflow**

* **What it Covered:** Securely running a data analysis script in **Google Colab**. This involved mounting **Google Drive** to access data, using Colab's built-in **secret manager** to handle an API key, and processing a CSV with **Pandas**.

* **Why you need it:** **Security and reproducibility.** You must never hardcode credentials (like API keys) in your code or notebooks. This teaches the industry-standard practice for managing sensitive data. Integrating Colab with Drive is a standard pattern for data scientists to work with datasets securely and efficiently in the cloud.

### **Question 5: Deploy a POST analytics endpoint to Vercel**

* **What it Covered:** Building and deploying a **serverless Python API** using **FastAPI** on **Vercel**. The endpoint accepted `POST` requests with a JSON payload, processed a dataset with Pandas, and returned calculated statistics.

* **Why you need it:** This represents a modern, scalable, and cost-effective way to build backends. **Serverless** (Vercel) abstracts away server management. **FastAPI** is a high-performance framework ideal for data APIs and machine learning model serving. This entire stack is perfect for building microservices that can handle unpredictable traffic without breaking the bank.

### **Question 6 & 7: Create a GitHub Action (with and without caching)**

* **What they Covered:** Automating software workflows with **GitHub Actions**. Question 6 covered the basics of setting up a CI/CD pipeline, while Question 7 introduced **dependency caching** to optimize it.

* **Why you need it:** Automation is the core of modern DevOps. CI/CD pipelines automatically build, test, and deploy your code, which dramatically reduces manual errors and speeds up development cycles. Caching (Q7) is crucial for efficiency, as it saves significant time and money on larger projects by not re-downloading dependencies on every run.

### **Question 8: Create and configure a Hugging Face Space**

* **What it Covered:** Configuring and deploying a containerized application to **Hugging Face Spaces** using the **Docker SDK**. This involved setting up a `Dockerfile`, defining application metadata and port settings in the `README.md`, and securely managing credentials using **HF Spaces Secrets**.

* **Why you need it:** Hugging Face Spaces is the premier platform for demonstrating Machine Learning models and data applications to a wide audience. While the standard SDKs (like Gradio/Streamlit) are great for simple apps, using the **Docker SDK** gives you maximum control and flexibility to deploy complex applications with specific dependencies, custom backends, or unique configurations. This skill is essential for MLOps engineers and data scientists who want to create robust, professional-grade ML demos.

### **Question 9: Push an image to Docker Hub**

* **What it Covered:** Containerizing an application using **Docker**. This involved writing a `Dockerfile`, building an image, tagging it, and pushing it to a public registry (**Docker Hub**).

* **Why you need it:** Docker is the industry standard for ensuring an application runs identically everywhere. It solves the "it works on my machine" problem. Pushing an image to a registry is the fundamental step for deploying applications to the cloud, sharing them with a team, or using them in a CI/CD pipeline. This is a cornerstone skill for backend, MLOps, and DevOps engineers.

### **Question 10: Configure a Codespace devcontainer**

* **What it Covered:** Creating a standardized, cloud-based development environment using **GitHub Codespaces** and a `devcontainer.json` configuration file.

* **Why you need it:** To ensure consistency across a development team. Devcontainers pre-configure the exact tools, extensions, and dependencies needed for a project. This eliminates environment setup headaches, accelerates onboarding for new developers, and guarantees that every team member is working in an identical setting.

### **Question 11: Write a FastAPI server to serve data**

* **What it Covered:** Using **FastAPI** to build a `GET` API endpoint that serves data from a CSV file, including support for filtering results using URL query parameters.

* **Why you need it:** This is a bread-and-butter task for data engineers and backend developers: making data accessible. Whether for a web dashboard, another microservice, or a business intelligence tool, exposing data through a clean, filterable API is a very common and necessary skill.

### **Question 12: FastAPI Google OAuth Login Verification**

* **What it Covered:** Implementing a secure "Sign in with Google" **(OAuth 2.0)** flow in a FastAPI application to authenticate users.

* **Why you need it:** You almost never build your own authentication system. Leveraging trusted third-party providers like Google is the standard for building secure, user-facing applications. This skill is critical for protecting user data and securing API endpoints that should only be accessible to logged-in users.

### **Question 13: Expose a local Ollama server with ngrok**

* **What it Covered:** Running a large language model (LLM) locally using **Ollama** and creating a secure public URL for it using **ngrok**. The task included advanced ngrok configuration to handle **CORS** policies and inject custom HTTP headers into responses.

* **Why you need it:** This demonstrates a powerful and common development pattern for rapid prototyping. It allows you to develop and test a front-end application against a real backend (like an LLM) without the cost and time of deploying the backend first. **ngrok** is an indispensable tool for testing webhooks, sharing local demos with clients or colleagues, and debugging complex cross-origin (CORS) issues in a controlled way.

## To learn more about these

* [Markdown](https://tds.s-anand.net/#/markdown) – Lightweight markup language for formatting text.
* [Image Compression](https://tds.s-anand.net/#/image-compression) – Techniques to reduce image file sizes without losing quality.
* [Static Hosting: GitHub Pages](https://tds.s-anand.net/#/github-pages) – Hosting static websites directly from a GitHub repository.
* [Notebooks: Google Colab](https://tds.s-anand.net/#/colab) – Cloud-based Jupyter notebooks for interactive coding and data analysis.
* [Serverless Hosting: Vercel](https://tds.s-anand.net/#/vercel) – Deploy web apps and APIs without managing servers.
* [CI/CD: GitHub Actions](https://tds.s-anand.net/#/github-actions) – Automate build, test, and deployment workflows.
* [Containers: Docker, Podman](https://tds.s-anand.net/#/docker) – Package applications and dependencies into portable containers.
* [DevContainers: GitHub Codespaces](https://tds.s-anand.net/#/github-codespaces) – Cloud development environments preconfigured with tools and dependencies.
* [HuggingFace Spaces](https://tds.s-anand.net/#/huggingface-spaces) – Host machine learning demos and apps online.
* [Tunneling: ngrok](https://tds.s-anand.net/#/ngrok) – Expose local servers to the internet securely for testing and development.
* [CORS](https://tds.s-anand.net/#/cors) – Browser security mechanism for cross-origin requests.
* [REST APIs](https://tds.s-anand.net/#/rest-apis) – Web service architecture for client-server communication using HTTP.
* [Web Framework: FastAPI](https://tds.s-anand.net/#/fastapi) – Python framework for building APIs with high performance.
* [Authentication: Google Auth](https://tds.s-anand.net/#/google-auth) – User authentication via Google accounts.
* [Local LLMs: Ollama](https://tds.s-anand.net/#/ollama) – Running large language models locally for inference and experimentation.
