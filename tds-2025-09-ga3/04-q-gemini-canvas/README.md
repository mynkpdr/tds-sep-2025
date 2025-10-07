# 4. Build and Share a Quiz App on Gemini Canvas (0.5 Marks)

## 1. Problem Description

Similar to the previous question, this task requires you to use Google's Gemini Canvas feature to create a simple, interactive quiz application. The final product should be a shareable link to your Gemini Canvas project.

## 2. Understanding the Requirements

* **Platform**: [Gemini](https://gemini.google.com/)
* **Feature**: Canvas
* **Content**: A working quiz application containing a specific question provided in the problem description.
* **Submission**: A public Gemini share URL (e.g., `https://gemini.google.com/share/...`).

## 3. Step-by-Step Solution

1. **Log in to Gemini**: Go to [https://gemini.google.com/](https://gemini.google.com/) and log in with your Google account.

2. **Open Canvas**: In the Gemini interface, look for an option to open or create a "Canvas". This provides a side-by-side view for code generation and preview.

3. **Write the Prompt**: Your prompt should be very specific. Ask Claude to create a complete, self-contained HTML file for a quiz app. You should specify the question, the options, and the correct answer. This helps Gemini generate exactly what you need.

4. **Generate and Preview**: Gemini will generate the code in one pane and a live preview in the other. You can immediately test the quiz functionality in the preview pane.

5. **Test the App**: If the quiz doesn't work correctly or you want to change the styling, you can give follow-up instructions to Gemini in the chat. For example, "Make the buttons larger and add a blue border."

6. **Share Your Work**: Once the quiz app is complete and working, find the "Share" option in the Gemini interface. This will create a public link to your work. It may look like `https://g.co/gemini/share/...` or `https://gemini.google.com/share/....`

7. **Submit the URL**: Copy the generated public URL for submission.

## 4. Code / Configuration File (Example Prompt for Gemini)

Let's assume the provided quiz question is "What do you call a triangle with all sides equal?" with the options "Equilateral", "Isosceles", "Scalene", "Right", and "Obtuse", where "Equilateral" is the correct answer.

```plaintext
Create a simple, self-contained quiz app in a single HTML file. The app should have one question. Use embedded CSS for clean styling and JavaScript for the logic.

The question is: "What do you call a triangle with all sides equal?"
The options are:
1. Equilateral
2. Isosceles
3. Scalene
4. Right
5. Obtuse

When the user selects an answer and clicks a "Check Answer" button, display a message indicating if their answer was "Correct!" or "Wrong!". The correct answer is "Equilateral".
```

## 5. How to Verify

1. **Visit the URL**: Open the Gemini share link you created in a web browser.
2. **Confirm Visibility**: The page should load and display your quiz, including the question and the multiple-choice options.
3. **Test the Logic**:
    * Click on "Equilateral" and submit. It should show a success message.
    * Click on "Scalene" or "Isosceles" and submit. It should show a failure message.
4. If the shared link works and the quiz functions as expected, your submission is correct.
