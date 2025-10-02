# 5. Deploy a POST analytics endpoint to Vercel (1 Marks)

## 1. Problem Description

The task is to deploy a serverless Python endpoint on Vercel. This endpoint must accept a `POST` request with a JSON payload, process a large dataset of telemetry pings (provided as a JSON file), and return calculated statistics for specified regions.

## 2. Understanding the Requirements

* **Platform**: Vercel.
* **Endpoint Behavior**:
  * Accepts `POST` requests.
  * Expects a JSON body like: `{"regions": ["...", "..."], "threshold_ms": ...}`.
  * Must handle the provided `q-vercel-latency.json` dataset.
* **Calculations**: For each region specified in the request, calculate:
  * `avg_latency`: Mean latency.
  * `p95_latency`: 95th percentile latency.
  * `avg_uptime`: Mean uptime.
  * `breaches`: Count of records where `latency_ms` exceeds `threshold_ms`.
* **CORS**: Must be enabled for `POST` requests from any origin (`*`).
* **Submission**: The public URL of the deployed Vercel endpoint.

## 3. Step-by-Step Solution

1. **Project Setup**:

      * Create a new project folder (e.g., `vercel-latency-api`).
      * Inside it, create an `api` sub-folder.
      * Download the `q-vercel-latency.json` file from the exam page and place it inside the `api` folder.

2. **Create the FastAPI App (`api/index.py`)**:

      * Inside the `api` folder, create a Python file named `index.py`.
      * This file will contain the FastAPI application, logic for loading the data, handling the `POST` request, and performing the calculations.
      * We will use `pandas` and `numpy` for efficient data processing.

3. **Create `requirements.txt`**:

      * In the root of your project folder (`vercel-latency-api`), create a `requirements.txt` file listing the dependencies.

4. **Create `vercel.json`**:

      * In the root of your project folder, create a `vercel.json` file to tell Vercel how to build and route requests to your Python app.

5. **Deploy to Vercel**:

      * Initialize a git repository, commit all files, and push to GitHub.
      * Go to [vercel.com](https://vercel.com) and create a new project, importing your GitHub repository. Vercel will automatically detect the configuration and deploy it.
      * Alternatively, use the Vercel CLI:

        ```bash
        # Install vercel cli if you haven't
        npm i -g vercel
        # Deploy from your project root
        vercel --prod
        ```

      * Once deployed, Vercel will provide you with a public URL. The endpoint URL will be `https://<your-app>.vercel.app/api/`. Copy this URL for submission.

## 4. Code / Configuration Files

#### `api/q-vercel-latency.json`

*This is the data file you download from the exam platform. Place it in the `api` directory.*

#### `api/index.py`

```python
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
from pathlib import Path

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Load the dataset once when the app starts
# The data file should be in the same directory as this script
DATA_FILE = Path(__file__).parent / "q-vercel-latency.json"
df = pd.read_json(DATA_FILE)


@app.get("/")
async def root():
    return {"message": "Vercel Latency Analytics API is running."}


@app.post("/api/")
async def get_latency_stats(request: Request):
    payload = await request.json()
    regions_to_process = payload.get("regions", [])
    threshold = payload.get("threshold_ms", 200)

    results = []

    for region in regions_to_process:
        region_df = df[df["region"] == region]

        if not region_df.empty:
            avg_latency = round(region_df["latency_ms"].mean(), 2)
            p95_latency = round(np.percentile(region_df["latency_ms"], 95), 2)
            avg_uptime = round(region_df["uptime_pct"].mean(), 3)
            breaches = int(region_df[region_df["latency_ms"] > threshold].shape[0])

            results.append(
                {
                    "region": region,
                    "avg_latency": avg_latency,
                    "p95_latency": p95_latency,
                    "avg_uptime": avg_uptime,
                    "breaches": breaches,
                }
            )

    return {"regions": results}

```

#### `requirements.txt`

```
fastapi
uvicorn
pandas
numpy
```

#### `vercel.json`

```json
{
  "builds": [{
    "src": "api/index.py",
    "use": "@vercel/python"
  }],
  "routes": [{
    "src": "/(.*)",
    "dest": "api/index.py"
  }]
}
```

## 5. Deploy to Vercel

1. **Create a Vercel Account**:

      * If you haven't already, sign up for a free account at [vercel.com](https://vercel.com).

2. **Install Vercel CLI**:

      * You can deploy your application using the Vercel CLI. Install it globally using npm:

        ```bash
        npm install -g vercel
        ```

3. **Deploy Your Application**:

      * From the root of your project directory, run the following command:

        ```bash
        > vercel --prod

          Vercel CLI 48.1.4
          ? Set up and deploy “~/q-vercel-latency”? yes
          ? Which scope should contain your project? mynkpdrs projects
          ? Link to existing project? no
          ? What’s your project’s name? q-vercel-latency
          ? In which directory is your code located? ./
          ? Do you want to change additional project settings? no
        ```

      * Follow the prompts to link your project to your Vercel account and deploy it.

4. **Get the Deployment URL**:

      * Once the deployment is complete, Vercel will provide you with a public URL for your API. This URL will be in the format `https://<your-app>.vercel.app/api/`.
      * Make sure the url is accessible and is public.

## 6. How to Run and Verify

You can test the endpoint locally before deploying using `uvicorn`:

```bash
# From the root directory, run:
uvicorn api.index:app --reload
```

Then, use a tool like `curl` or Postman to send a `POST` request to `http://127.0.0.1:8000/api/`:

```bash
curl -X POST http://127.0.0.1:8000/api/ \
-H "Content-Type: application/json" \
-d '{"regions": ["emea", "apac"], "threshold_ms": 180}'
```

The final verification is done by the exam platform, which will `POST` its own payload to your submitted Vercel URL and check if the returned JSON matches the expected calculations.
