# 4. LLM Vision (1 Mark)

## 1. Problem Description

The task is to write a JSON request body for the OpenAI API that asks a "vision model" (`gpt-4o-mini`) to analyze an image and extract any text it sees. This involves sending both a text instruction and the image data in a single request.

## 2. Understanding the Requirements

- **Output Format**: A single, valid JSON object.
- **Model**: Must be `gpt-4o-mini`.
- **Message Structure**: The request must contain a single `user` message.
- **Content Structure**: The `content` of the user message must be an array containing two parts, in a specific order:
  1. A `text` part with the instruction: `Extract text from this image`.
  2. An `image_url` part containing the image data.
- **Image Data**: The image must be sent as a **base64 data URL**, which is provided in the question itself. You must use the exact URL from the image on the page.

## 3. Step-by-Step Solution

1. **Find the Image Data URL**:
   - On the question page, locate the example image.
   - Right-click the image and select "Copy Image Address" or "Copy Image Link".
   - Alternatively, you can also right-click and "Inspect" the image. The developer tools will show the `<img>` tag, and you can copy the full value of the `src` attribute.
   - The copied URL should start with `data:image/png;base64,` followed by a very long string of characters. This entire string is the data URL.

2. **Start the JSON Structure**: Begin with the main curly braces `{}` and define the top-level keys: `"model"` and `"messages"`.

3. **Fill in the Model**: Set the model name: `"model": "gpt-4o-mini"`.

4. **Construct the `messages` Array**:
   - The `messages` key will have an array `[...]` as its value, containing just one object.
   - This object represents the user message: `{"role": "user", "content": [...]}`.

5. **Construct the `content` Array**: This is the core of the task. The `content` array must have two objects inside it:
   - **First Object (Text)**: `{"type": "text", "text": "Extract text from this image"}`.
   - **Second Object (Image)**: `{"type": "image_url", "image_url": {"url": "..."}}`.
     - In place of `...`, paste the full base64 data URL you copied in Step 1.

6. **Assemble and Validate**: Combine all the parts into a single JSON object. Be careful with commas, quotes, and braces. You can use an online JSON validator to ensure your syntax is correct before submitting.

## 4. Code / Configuration File

This is the final JSON body to be submitted. The base64 string is truncated here for readability.

```json
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Extract text from this image"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAl......"
          }
        }
      ]
    }
  ]
}
```

_Note_: Your task is to provide the JSON to _ask_ the AI to extract this text, not to provide the extracted text itself.

## 5. How to Verify

The platform will automatically parse and validate your submitted JSON. It will check:

- If the `model` is `gpt-4o-mini`.
- If there is exactly one message with the `role` of `user`.
- If the message `content` is an array with two parts.
- If the first part is `text` with the correct instruction.
- If the second part is `image_url`.
- If the `url` inside `image_url` exactly matches the base64 data URL from the question's image.
