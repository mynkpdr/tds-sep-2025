# 5. LLM Embeddings (0.5 Marks)

## 1. Problem Description

The task is to create the JSON body for a request to the OpenAI Embeddings API. An "embedding" is a numerical representation (a vector) of text that captures its semantic meaning. This request will ask the `text-embedding-3-small` model to generate embeddings for two specific sentences provided in the problem.

## 2. Understanding the Requirements

- **API Endpoint**: The request is for the embeddings endpoint (`/v1/embeddings`).
- **Model**: The model must be `text-embedding-3-small`.
- **Input**: The JSON body must contain an `input` key.
- **Input Format**: The value of the `input` key must be an array containing the two sentences from the question, exactly as they are written.

## 3. Step-by-Step Solution

1. **Copy the Input Texts**: Go to the question page and carefully copy the two transaction verification messages. Pay close attention to spacing, numbers, and the email address, as they must be identical.

2. **Start the JSON Structure**: An embeddings request is simpler than a chat request. Start with an empty JSON object `{}`.

3. **Add the `model` Key**: The first key-value pair is for the model.
   - `"model": "text-embedding-3-small"`

4. **Add the `input` Key**: The second key-value pair is for the input text.
   - The value for `"input"` must be a JSON array (using square brackets `[]`).
   - Inside the array, add the two sentences you copied, each as a separate string enclosed in double quotes.

5. **Assemble and Validate**: Combine the parts into the final JSON. Ensure there's a comma between the `model` and `input` pairs. Use a JSON validator to check for syntax errors.

## 4. Code / Configuration File

This is the complete JSON request body to be submitted.

```json
{
  "model": "text-embedding-3-small",
  "input": [
    "Dear user, please verify your transaction code 53689 sent to 23f3004197@ds.study.iitm.ac.in",
    "Dear user, please verify your transaction code 14380 sent to 23f3004197@ds.study.iitm.ac.in"
  ]
}
```

_(**Note**: The transaction codes `53689` and `14380` are examples. You must use the exact sentences and codes provided in your specific version of the question.)_

## 5. How to Verify

The exam system will parse your submitted JSON and check for correctness:

- Is it valid JSON syntax?
- Is the `model` specified correctly as `text-embedding-3-small`?
- Does the `input` key exist and is its value an array of two strings?
- Do the two strings in the array match the required sentences from the question _exactly_?
