# 3. POST HTTP requests with uv (0.4 Marks)

Great! Let’s go **step by step** to run this eShopCo API health check using `uv` and `httpie`.

---

## **Step 1: Install `uv` (if not already installed)**

### Using `pip`

```bash
pip install uv
```

Or if you already have `uvx` installed as part of `uv`, it’s ready to run.

---

## **Step 2: Run the API POST request**

Open your terminal and type exactly:

```bash
uv run --with httpie -- http --json POST https://httpbin.org/post email=23f3004197@ds.study.iitm.ac.in request_id=8127ed21
```

* `--with httpie` tells `uv` to run the script using HTTPie.
* `--` separates `uv` options from the command being run.
* `http --json POST ...` is the HTTPie command to POST a JSON payload.

---

## **Step 3: Understand the response**

* HTTPie will return a JSON object.
* Look for the **`json` field** in the response. It should echo your payload:

Example output:

```json
{
    "args": {},
    "data": "{\"email\": \"23f3004197@ds.study.iitm.ac.in\", \"request_id\": \"8127ed21\"}",
    "files": {},
    "form": {},
    "headers": {
        "Accept": "application/json, */*;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "69",
        "Content-Type": "application/json",
        "Host": "httpbin.org",
        "User-Agent": "HTTPie/3.2.4",
        "X-Amzn-Trace-Id": "Root=1-68d50561-2a1a95390f6ee37b65d78b36"
    },
    "json": {
        "email": "23f3004197@ds.study.iitm.ac.in",
        "request_id": "8127ed21"
    },
    "origin": "0.0.0.0",
    "url": "https://httpbin.org/post"
}
```

✅ **Important:** Copy the **entire JSON output** and paste it as requested.
