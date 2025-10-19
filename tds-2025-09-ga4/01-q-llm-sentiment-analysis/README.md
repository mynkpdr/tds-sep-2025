# 1. LLM Sentiment Analysis (0.5 Marks)

## 1. Problem Description

The goal of this task is to write a Python program that analyzes the sentiment of a piece of text. The program will send the text to an AI model (specifically, OpenAI's API) and ask it to classify the sentiment as GOOD, BAD, or NEUTRAL.

## 2. Understanding the Requirements

- **Language**: Python
- **Library**: The code must use the `httpx` library to make a web request.
- **API Call**: The program needs to make an HTTP `POST` request to an OpenAI-compatible API endpoint for chat completions.
- **Authentication**: The request must include an `Authorization` header with a dummy API key.
- **Model**: The AI model to be used is `gpt-4o-mini`.
- **Messages**: The request must contain two messages for the AI:
  1. A "system" message that instructs the AI on how to classify the sentiment (mentioning the categories GOOD, BAD, and NEUTRAL).
  2. A "user" message that contains the exact text to be analyzed, as provided in the problem description.

## 3. Step-by-Step Solution

1. **Import the Library**: Start your Python script by importing the `httpx` library, which is used for making HTTP requests.
2. **Define API Details**:
   - Set the `url` for the OpenAI chat completions endpoint. A common URL is `https://api.openai.com/v1/chat/completions`.
   - Create a `headers` dictionary. Inside it, add an `Authorization` key. The value can be a fake key like `"Bearer DUMMY_API_KEY"`.
3. **Get the Text to Analyze**: Copy the meaningless text provided in the question's `<pre>` block exactly as it is.
4. **Construct the Request Body**:
   - Create a Python dictionary called `data` or `payload`.
   - Set the `"model"` key to `"gpt-4o-mini"`.
   - Add a `"messages"` key. Its value should be a list of two dictionaries:
     - **First message (system)**: `{"role": "system", "content": "You are a sentiment analysis assistant. Classify the text as GOOD, BAD, or NEUTRAL."}`
     - **Second message (user)**: `{"role": "user", "content": "..."}` where `...` is the meaningless text you copied.
5. **Make the API Call**:
   - Use `httpx.post()` to send the request.
   - Pass the `url`, `headers`, and `json=data` as arguments.
   - Store the result in a `response` variable.
6. **Review the Code**: Double-check that all requirements are met: the model name is correct, the messages are in the right order, and the headers are set up properly. The code in the next section is a complete, working example.

## 4. Code / Configuration File

This is the Python code you should write to solve the problem.

```python
import httpx

# 1. API endpoint URL
url = "https://api.openai.com/v1/chat/completions"

# 2. Authorization header with a dummy API key
headers = {
    "Authorization": "Bearer DUMMY_API_KEY",
    "Content-Type": "application/json"
}

# 3. The specific text to be analyzed (copy this from the question page)
text_to_analyze = """Uu  qbT 6w  YYbEbtU I  cZ6G84mNCNR kME
 KL 7G1LX C""" # Example text

# 4. The JSON body for the POST request
data = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "system",
            "content": "Analyze the sentiment of the following text and classify it as GOOD, BAD, or NEUTRAL."
        },
        {
            "role": "user",
            "content": text_to_analyze
        }
    ]
}

# 5. Sending the POST request
response = httpx.post(url, headers=headers, json=data)
print(response.json())

```

## 5. How to Verify

For this specific question, you don't need to actually run the code and see a response. The exam platform will automatically test your code against a simulated environment. It will check if your script attempts to make a `POST` request to the correct URL with the correct headers and JSON body structure as specified in the requirements.
