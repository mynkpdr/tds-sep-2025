from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from pydantic import BaseModel


app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # Allows all origins
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]    # Expose all the headers to the browser in response
)


class CheckRequest(BaseModel):
    regions: List[str]
    threshold_ms: int


# REQUEST:->         {"regions":["amer","emea"],"threshold_ms":152}
# RESPONSE:->        {"regions":{"amer":{"avg_latency":176.27,"p95":220.86,"avg_uptime":97.98,"breaches":9},"emea":{"avg_latency":177.2,"p95":218.3,"avg_uptime":98.5,"breaches":8}}}

@app.post("/check")
def check(data: CheckRequest):
    regions = data.regions
    threshold_ms = data.threshold_ms

    import json
    import os

    file = "q-vercel-latency.json"
    path = os.path.join(os.path.dirname(__file__), file)
    with open(path, "r") as f:
        telemetry = json.load(f)

    result = {}

    for region in regions:
        latency_sum = 0
        uptime_sum = 0
        breaches = 0
        count = 0

        for entry in telemetry:
            if entry["region"] == region:
                latency_sum += entry["latency_ms"]
                uptime_sum += entry["uptime_pct"]
                count += 1
                if entry["latency_ms"] > threshold_ms:
                    breaches += 1

        avg_latency = round(latency_sum / count, 2) if count else 0
        avg_uptime = round(uptime_sum / count, 2) if count else 0
        import numpy as np

        region_latencies = [e["latency_ms"] for e in telemetry if e["region"] == region]
        p95 = np.percentile(region_latencies, 95) if region_latencies else 0

        result[region] = {
            "avg_latency": round(avg_latency, 2),
            "p95": round(p95, 2),
            "avg_uptime": round(avg_uptime, 2),
            "breaches": breaches,
        }
    return {"regions": result}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
