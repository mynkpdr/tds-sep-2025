# 6. Multimodal Embeddings (0.5 Marks)

> [!WARNING]  
> **This solution is having a problem and may not work for all**

## 1. Problem Description

This task requires you to calculate the "similarity score" between an image and a short text description. This is done using a "multimodal embedding" model, which can understand and represent both images and text in the same numerical space. The similarity score is calculated as the dot product of their respective embedding vectors.

## 2. Understanding the Requirements

- **Model**: You must use Jina AI's `jina-clip-v2` model.
- **Calculation**:
  1. Generate an embedding vector for the given image.
  2. Generate an embedding vector for the given text phrase.
  3. Calculate the dot product of these two vectors.
- **Output**: The final answer is a single number (the similarity score), which should be formatted with at least 4 decimal places.
- **API Key**: This task requires an API key from Jina AI.

## 3. Step-by-Step Solution

### Step 1: Get a Jina AI API Key

1. Go to the Jina AI Embeddings page: [https://jina.ai/embeddings/](https://jina.ai/embeddings/).
2. Click "Get Started" and sign up for a free account.
3. Navigate to your dashboard, find the "API Key & Billing" section, and copy your API key.

### Step 2: Prepare the Image and Text

1. **Text**: Copy the text description exactly as it appears in the question (e.g., `Dialectique hégélienne transcendantale`).
2. **Image**: The image is provided as a base64 data URI.
   - Right-click the image in the question and select "Copy Image Address".

### Step 3: Prepare and Run the Python Script

Instead of using multiple tools, the provided Python script will handle everything: making the API call, getting the embeddings, and calculating the final score.

1. **Save the Code**: Copy the complete Python code from the "Code / Configuration File" section below and save it in a file named `calculate.py`.
2. **Fill in the Details**: Open `calculate.py` and replace the placeholder values for `JINA_API_KEY`, `TEXT_PROMPT`, and `IMAGE_B64` with your actual API key and the text/image data you prepared in Step 2.
3. **Install Libraries**: If you don't have them, install `httpx` and `numpy`.

   ```bash
   pip install httpx numpy
   ```

4. **Run the Script**: Execute the script from your terminal.

   ```bash
   python calculate.py
   ```

### Step 4: Submit the Answer

The script will print the final similarity score. Copy this number and paste it into the answer box on the exam page.

## 4. Code / Configuration File

This Python script (`calculate.py`) performs the API call and the dot product calculation. **You must edit the placeholder values in this script.**

```python
import httpx
import numpy as np

# --- YOU MUST EDIT THESE THREE VARIABLES ---
# 1. Paste your Jina AI API Key here
JINA_API_KEY = "your-jina-api-key-here"

# 2. Paste the exact text phrase from the question here
TEXT_PROMPT = "Your text phrase from the question"

# 3. Paste the long base64 string from the image here
IMAGE_B64 = "...the long base64 string from the image..."
# -----------------------------------------

IMAGE_B64 = IMAGE_B64.removeprefix("data:image/webp;base64,")  # Clean the base64 string if it has a prefix

# API endpoint and headers
url = "https://api.jina.ai/v1/embeddings"
headers = {
    "Authorization": f"Bearer {JINA_API_KEY}",
    "Content-Type": "application/json"
}

# JSON payload for the request
payload = {
    "model": "jina-clip-v2",
    "input": [
        {"text": TEXT_PROMPT},
        {"image": IMAGE_B64}
    ]
}

try:
    # Make the API call
    response = httpx.post(url, headers=headers, json=payload)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

    data = response.json()

    # The response contains a list of embeddings in the same order as the input
    # First result is for the text, second is for the image
    text_embedding = data['data'][0]['embedding']
    image_embedding = data['data'][1]['embedding']

    # Calculate the dot product (which is the cosine similarity for normalized vectors)
    similarity_score = np.dot(text_embedding, image_embedding)

    # Print the result formatted to several decimal places
    print(f"Similarity Score: {similarity_score:.6f}")

except Error as e:
    print(f"An error occurred: {e}")

```

## 5. How to Verify

Just submit the similarity score printed by the script. The platform will check if your submitted number matches the pre-calculated correct answer.
