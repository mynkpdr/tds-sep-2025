# 5. Build an App Using GitHub Copilot Chat (0.5 Marks)

## 1. Problem Description

The task is to use the GitHub Copilot Chat extension in Visual Studio Code to generate a simple quiz application. The final submission is not the app itself, but the entire chat log from the "Output" channel in VS Code, which documents your interaction with Copilot.

## 2. Understanding the Requirements

- **Tool**: Visual Studio Code (VS Code).
- **Extension**: GitHub Copilot Chat.
- **Task**: Instruct Copilot to create a simple quiz application.
- **Submission**: The full, unmodified text content from the "GitHub Copilot Chat" output channel.

## 3. Step-by-Step Solution

1. **Setup VS Code**: Ensure you have VS Code installed and the `GitHub.copilot-chat` extension is installed and enabled from the Marketplace. You must be logged in with your GitHub account.

2. **Create a Project Folder**: Create a new folder on your computer, for example `copilot-quiz`, and open it in VS Code.

3. **Open Copilot Chat**: Press `Ctrl+Shift+I` (or `Cmd+Shift+I` on Mac) to open the Copilot Chat.

4. **Interact with Copilot**: Type a prompt in the chat box asking Copilot to create a quiz. For example, you can ask it to create an `index.html` file with the quiz content.

5. **Generate the File**: Copilot will suggest code. You can accept it to create the `index.html` file. You can have a small conversation to refine it if you wish. The goal is simply to generate some interaction in the log.

6. **Find the Output Channel**:

    - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the Command Palette.
    - Type `Output: Show Output Channels...` and press Enter.
    - You may get an option to select the output channel. Select `GitHub Copilot Chat`.

7. **Copy the Log**: The panel will now display the detailed log of your session. Click inside the panel, select all the text (`Ctrl+A` or `Cmd+A`), and copy it (`Ctrl+C` or `Cmd+C`).

8. **Submit**: Paste the copied log text as your answer.

## 4. Code / Configuration File (Example Prompt for Copilot)

This is the prompt you would type into the Copilot Chat panel in VS Code.

```bash
@workspace /new index.html Please create a simple quiz in a single HTML file. The question is "What is the national animal of India?". The options are "Tiger", "Lion", "Elephant", "Peacock" and "Bear". The correct answer is "Tiger".
```

## 5. How to Verify

The submission is the log itself. The automated checker will scan the log for specific markers that prove you used the extension correctly. You can quickly verify your log by checking for the presence of lines that look like this:

- Evidence of authentication: `Got Copilot token for <your-github-username>`
- Evidence of chat requests: `ccreq:xxxxxxxx.copilotmd`
- Evidence of model metadata: `Fetched model metadata in...`

If your log is long and contains these types of technical entries, it is likely correct. Do not edit or trim the log; submit the entire content.
