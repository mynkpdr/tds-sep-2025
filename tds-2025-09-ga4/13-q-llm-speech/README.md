# 13. LLM Speech (0.25 Marks)

## 1. Problem Description

The task is to write the JSON body for a request to the OpenAI Text-to-Speech (TTS) API. This API converts written text into spoken audio. Your JSON object will specify all the details for this conversion, including the AI model, the voice to use, the speaking speed, and the text to be spoken.

## 2. Understanding the Requirements

- **Output Format**: A single, valid JSON object.
- **API Endpoint**: The request is for the audio speech endpoint (`/v1/audio/speech`).
- **Parameters**: Your JSON must be constructed with specific key-value pairs, whose values are provided in your unique version of the question.
  - `model`: The name of the TTS model (e.g., `tts-1` or `tts-1-hd`).
  - `input`: The exact text to be converted into speech.
  - `voice`: The name of the voice to use (e.g., `alloy`, `sage`).
  - `speed`: The speed of the speech (a number between 0.25 and 4.0).
  - `response_format`: The desired audio file format (e.g., `mp3`, `aac`).

## 3. Step-by-Step Solution

1. **Gather the Required Values**: Carefully read the question on the exam page and note the exact values for each parameter.
   - **Model**: (e.g., `tts-1-hd`)
   - **Voice**: (e.g., `sage`)
   - **Speed**: (e.g., `1.4`)
   - **Response Format**: (e.g., `aac`)
   - **Input Text**: (e.g., `This is a test of the OpenAI text-to-speech API. The current time is approximately 12:19:42 PM.`)

2. **Start the JSON Object**: Begin with an empty JSON object `{}`.

3. **Add Key-Value Pairs**: For each parameter, add a key and its corresponding value to the JSON object.
   - `"model": "..."` (The value is a string)
   - `"input": "..."` (The value is a string, copied exactly from the question)
   - `"voice": "..."` (The value is a string)
   - `"speed": ...` (The value is a number, so it should **not** be enclosed in quotes)
   - `"response_format": "..."` (The value is a string. This may be optional if the default `mp3` is required, but it is best to include it).

4. **Assemble and Validate**: Combine all the pairs, separating them with commas. Ensure the last pair does not have a trailing comma. You can use an online JSON validator to check for any syntax errors before submitting.

## 4. Code / Configuration File

This is an example of the final JSON body. You must replace the values below with the specific ones from your question.

```json
{
  "model": "tts-1-hd",
  "input": "This is a test of the OpenAI text-to-speech API. The current time is approximately 12:19:42 PM.",
  "voice": "sage",
  "speed": 1.4,
  "response_format": "aac"
}
```

## 5. How to Verify

The exam platform will parse your submitted text as a JSON object and perform several checks:

- Is the JSON syntax valid?
- Are all the required keys (`model`, `input`, `voice`, `speed`) present?
- Does the value for each key exactly match the value specified in your unique version of the question?
