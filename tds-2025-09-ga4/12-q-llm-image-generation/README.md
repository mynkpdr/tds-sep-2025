# 12. LLM Image Generation (0.25 Marks)

## 1. Problem Description

The task is to write a JSON request body for the OpenAI Image Generation API. This JSON object will contain all the necessary instructions for the AI to create a specific image, including which model to use, the size of the image, how many images to generate, and a textual description (the prompt) of the image content.

## 2. Understanding the Requirements

- **Output Format**: A single, valid JSON object.
- **API Endpoint**: The request is for the image generations endpoint (`/v1/images/generations`).
- **Parameters**: Your JSON must include several specific key-value pairs. The exact values for these parameters are provided in your unique version of the question. You must use them exactly as specified.
  - `model`: The name of the AI model (e.g., `gpt-image-1`).
  - `prompt`: The detailed text description of the image to create.
  - `n`: The number of images to generate (an integer).
  - `size`: The dimensions of the image (e.g., `1024x1024`).
  - `response_format`: How the API should return the image data (e.g., `url` or `b64_json`).

## 3. Step-by-Step Solution

1. **Read the Requirements Carefully**: Go to the question page and identify the exact values required for each parameter. Write them down or copy them to a text editor.
   - **Model**: (e.g., `gpt-image-1`)
   - **Size**: (e.g., `512x512`)
   - **Number of images (n)**: (e.g., `2`)
   - **Response Format**: (e.g., `url`)
   - **Prompt**: (e.g., "A whimsical illustration of a cat playing chess with an owl")

2. **Start the JSON Structure**: Begin with an empty JSON object `{}`.

3. **Add Each Key-Value Pair**: Add each required parameter to the JSON object.
   - `"model": "..."` (The value must be a string)
   - `"prompt": "..."` (The value must be a string, copied exactly)
   - `"n": ...` (The value must be an integer, **not** in quotes)
   - `"size": "..."` (The value must be a string)
   - `"response_format": "..."` (The value must be a string. Note: if the required format is `url`, this key is optional as it's the default, but it's good practice to include it explicitly).

4. **Assemble and Validate**: Combine all the key-value pairs, making sure to separate each pair with a comma. The last pair should not have a comma after it. Use an online JSON validator to check your syntax.

## 4. Code / Configuration File

This is an example of the final JSON body. You must replace the values with those specified in your question.

```json
{
  "model": "gpt-image-1",
  "prompt": "A serene landscape with mountains and a lake at sunset, digital art style",
  "n": 1,
  "size": "1024x1024",
  "response_format": "url"
}
```

**Another Example (with different requirements):**

```json
{
  "model": "gpt-image-1-mini",
  "prompt": "A futuristic cityscape with flying cars and neon lights, cyberpunk style",
  "n": 1,
  "size": "512x512",
  "response_format": "b64_json"
}
```

## 5. How to Verify

The exam platform will parse your submitted text as JSON and verify that:

- It is a syntactically valid JSON object.
- All required keys (`model`, `prompt`, `n`, `size`, etc.) are present.
- The value for each key exactly matches what was specified in your unique version of the question.
