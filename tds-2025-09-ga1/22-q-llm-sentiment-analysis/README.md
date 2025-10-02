# 22. LLM Sentiment Analysis (0.4 Marks)

Objective
---------

Write a Python script using a mocked `httpx` library to send a correctly formatted POST request to an OpenAI-compatible API for sentiment analysis.

The Task
--------

You need to write a Python script that constructs a specific API request. The validation happens inside a simulated environment (Pyodide), so you don't need a real API key or internet connection. The script simply needs to demonstrate that you know how to structure the request.

### Key Requirements for the Request

1. **Method:** It must be a `POST` request.

2. **Library:** It must use the (mocked) `httpx` library, specifically `httpx.post(...)`.

3. **Endpoint:** The URL must end with `/v1/chat/completions`.

4. **Headers:** Must include an `Authorization` header (the value can be a dummy key like `"Bearer DUMMY_KEY"`).

5. **Body:** The request must have a JSON body with the following structure:

    - `model`: The value must be exactly `gpt-4o-mini`.

    - `messages`: A list containing two dictionaries:

        1. **System Message:**  `role` is `system`, and `content` is a string that instructs the model to classify sentiment into `GOOD`, `BAD`, or `NEUTRAL`.

        2. **User Message:**  `role` is `user`, and `content` is the **exact** meaningless text provided in the quiz prompt.

### Solution Script

The following Python script correctly constructs the required request. The `text_to_analyze` variable must be replaced with the unique text generated for you in the quiz. For example:

```
Uu  qbT 6w  YYbEbtU I  cZ6G84mNCNR kME
 KL 7G1LX C
```

```python
import httpx
import json

# --- Personalized Data ---
# Replace with the text from your quiz prompt
text_to_analyze = """
Uu  qbT 6w  YYbEbtU I  cZ6G84mNCNR kME
 KL 7G1LX C
"""
# Make sure to include the exact text provided in your quiz prompt
# -------------------------

# The API endpoint (can be a placeholder)
API_URL = "https://api.openai.com/v1/chat/completions"

# A dummy API key is sufficient for this mock environment
HEADERS = {
    "Authorization": "Bearer sk-dummy-key-for-testing",
    "Content-Type": "application/json"
}

# The JSON body for the request
DATA = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "system",
            "content": "Analyze the sentiment of the following text. Classify it as GOOD, BAD, or NEUTRAL."
        },
        {
            "role": "user",
            "content": text_to_analyze
        }
    ]
}

# Make the POST request using the mocked httpx library
# The quiz environment intercepts this call and checks its structure.
response = httpx.post(url=API_URL, headers=HEADERS, json=DATA)

# You can optionally print the (mocked) response
# In the actual quiz, these lines aren't necessary for validation
# but are good practice.
# response.raise_for_status()
# print(response.json())

```

**To get the answer, simply paste the complete Python script into the answer box.**
