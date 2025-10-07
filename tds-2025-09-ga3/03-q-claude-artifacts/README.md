# 3. Build and Share a Quiz App on Claude Artifacts (0.5 Marks)

## 1. Problem Description

The task is to use Claude's "Artifacts" feature to create a simple, interactive quiz application. The quiz should be contained in a single HTML file with embedded CSS and JavaScript. After creating the app, you need to share it and submit the public URL.

## 2. Understanding the Requirements

- **Platform**: [Claude.ai](https://claude.ai/)
- **Feature**: Artifacts
- **Content**: A functional quiz app. The specific question for the quiz will be provided during the task.
- **Submission**: A public Claude Artifacts URL (e.g., `https://claude.ai/public/artifacts/...`).

## 3. Step-by-Step Solution

1. **Log in to Claude**: Navigate to [https://claude.ai/](https://claude.ai/) and log in to your account.

2. **Start a New Chat**: Begin a new conversation with Claude.

3. **Write the Prompt**: Your prompt should be very specific. Ask Claude to create a complete, self-contained HTML file for a quiz app. You should specify the question, the options, and the correct answer. This helps Claude generate exactly what you need.

4. **Generate the Artifact**: After you send the prompt, Claude will generate the code. Because the code is a self-contained HTML file, Claude will automatically open it as an "Artifact" in a new panel next to the chat.

5. **Test the App**: You can interact with the quiz directly in the Artifacts panel to make sure it works as expected. If it doesn't, you can ask Claude to make changes, and the artifact will update in real-time. For example, "Change the color of the 'Correct!' message to green."

6. **Share the Artifact**: Once you are satisfied with the app, find the "Publish" button associated with the artifact panel. This will generate a public URL.

7. **Submit the URL**: Copy the public URL and submit it as your answer.

## 4. Code / Configuration File (Example Prompt for Claude)

Let's assume the provided quiz question is "What is the name of the Indian space agency?" with the options "ISRO", "NASA", "ESA", "JAXA", and "Roscosmos", where "ISRO" is the correct answer.

```plaintext
Create a simple, self-contained quiz app in a single HTML file. The app should have one question. Use embedded CSS for clean styling and JavaScript for the logic.

The question is: "What is the name of the Indian space agency?"
The options are:
1. ISRO
2. NASA
3. ESA
4. JAXA
5. Roscosmos

When the user selects an answer and clicks a "Check Answer" button, display a message indicating if their answer was "Correct!" or "Wrong!". The correct answer is "ISRO".
```

## 5. How to Verify

1. **Open the URL**: Paste the public URL you generated (e.g., `https://claude.ai/public/artifacts/...`) into your browser.
2. **Check Content**: The quiz application should load and display the question and options.
3. **Test Functionality**:
    - Select the correct answer. For example, ("ISRO") and click the button. You should see a "Correct!" message.
    - Select a wrong answer and click the button. You should see a "Wrong!" message.
4. If the app loads and functions correctly, your submission is valid.
