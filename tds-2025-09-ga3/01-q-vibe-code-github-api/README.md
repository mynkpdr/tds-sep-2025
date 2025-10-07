# 1. Vibe Code a GitHub API App (0.5 Marks)

## 1. Problem Description

The task is to write a prompt for an AI model (like GPT-5 Nano) that generates the body of a JavaScript function. This function must fetch a GitHub user's account creation date from the public GitHub API. The key challenge is to create a prompt that guides the AI without explicitly stating the function names or URLs to be used, a practice known as "avoiding spoonfeeding."

## 2. Understanding the Requirements

* **Output Format**: The AI's response should only be the body of a JavaScript function.
* **Function Signature**: The generated code should assume a variable named `user` (the GitHub username) is available in its scope.
* **Core Logic**: The function must:
    1. Make an asynchronous request to the public GitHub API endpoint for user profiles.
    2. Receive and parse the JSON response.
    3. Extract and return the value of the `created_at` field.

## 3. Step-by-Step Solution

1. **Analyze the Goal**: The main objective is to get a specific piece of data (`created_at`) from a specific source (GitHub's user API). The code needs to handle an external web request, process data, and return a value.

2. **Deconstruct the Logic**:
    * It needs to construct a URL for a specific GitHub user.
    * It needs to perform an HTTP GET request to that URL.
    * It needs to handle the response, which is in JSON format.
    * It needs to access a specific key in the resulting JSON object.
    * It needs to response with the body inside the function.

3. **Formulate the Prompt**: The prompt should describe the *what* (the goal) rather than the *how* (the specific code). We'll use descriptive, high-level language.
    * Instead of `await fetch("api.github.com/...")`, we can say "retrieve the user's public profile data from GitHub's user API".
    * Instead of `return data.created_at`, we can say "return the value of the account creation date field".

4. **Combine into the Final Prompt**: Combining these ideas gives us a prompt that is clear in its intent but does not give away the specific implementation details, forcing the AI to deduce the correct approach. This is the final answer you will submit.

## 4. Code / Configuration File (The Prompt)

This is the prompt you would provide to the AI model and most likely to work.

```
Write the body of an async JavaScript function that takes a GitHub username in a variable called "user". The body should retrieve the user's public profile data from GitHub's user API, parse the JSON response, and return the value of the account creation date field.

Make sure you are not including the async function, just the body inside it.
```

## 5. How to Verify

You can verify the AI-generated code from the network tab.

1. Open your browser's developer tools (usually F12 or right-click and select "Inspect").
2. Go to the "Network" tab.
3. Verify that the AI-generated code makes a request to `https://api.github.com/users/{user}`.
4. You will see a random user request next to the URL with a `200` status code.
