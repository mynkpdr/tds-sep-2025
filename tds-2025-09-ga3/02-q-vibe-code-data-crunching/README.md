# 2. Vibe Code a Data Crunching App (0.5 Marks)

## 1. Problem Description

The goal is to write a prompt for an AI model that generates the body of a JavaScript function. This function needs to fetch a JSON dataset from a given URL, process it by summing up specific numerical values within the data, and return the total sum.

## 2. Understanding the Requirements

* **Output Format**: The AI must generate only the body of a JavaScript function.
* **Function Signature**: The code should assume a variable named `url` is available in its scope.
* **Core Logic**: The function must:
    1. Fetch data from the provided `url`.
    2. Parse the response as JSON. The JSON structure will contain a `data` key, which is an array of objects.
    3. Iterate through the `data` array and sum the values of the `number` key in each object.
    4. Return the final calculated sum.

## 3. Step-by-Step Solution

1. **Analyze the Goal**: The core task is to download structured data, extract numbers from it, and compute their sum. This involves asynchronous operations, data parsing, and data aggregation (summation).

2. **Formulate the Prompt**: We need to describe the task in a way that implies the necessary steps without naming the specific JavaScript methods (Spoonfeeding).
    * To imply fetching data from a URL, we can say "retrieve content from this URL".
    * To imply parsing JSON, we can say "interpret it as a JSON object".
    * To imply the summation logic, we can describe the aggregation process: "calculate the total sum of the "number" property for each element".

3. **Combine into the Final Prompt**: Assembling these high-level descriptions results in a complete prompt that guides the AI effectively. This prompt is the final answer to be submitted.

## 4. Code / Configuration File (The Prompt)

This is the prompt you would provide to the AI model and most likely to work.

```plaintext
Write the body for an async JavaScript function. This function should accept a "url" variable. It should retrieve content from this URL, interpret it as a JSON object, and calculate the total sum of the "number" property for each element within the top-level "data" array. Finally, it should return the computed sum.

Make sure you are not including the async function, just the body inside it
```

## 5. How to Verify

You can verify the AI-generated code from the network tab.
