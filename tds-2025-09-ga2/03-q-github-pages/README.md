# 3. Host your portfolio on GitHub Pages (0.5 Marks)

## 1. Problem Description

The task is to publish a simple static webpage using GitHub Pages. The webpage's HTML must contain your email address, `23f3004197@ds.study.iitm.ac.in`, wrapped in special comments to prevent email obfuscation by Cloudflare.

## 2. Understanding the Requirements

* **Hosting Platform**: GitHub Pages.
* **Content**: The page must include the email `23f3004197@ds.study.iitm.ac.in`.
* **Email Format**: The email must be wrapped in `<!--email_off-->` and `<!--/email_off-->` comments.
* **Submission**: You need to provide the final public URL of your GitHub Pages site (e.g., `https://<user>.github.io/<repo>/`).

## 3. Step-by-Step Solution

1. **Create a GitHub Repository**:
    * Log in to your GitHub account.
    * Create a new public repository. Let's name it `my-portfolio`.

2. **Create the HTML File**:
    * On your local machine, create a new file named `index.html`.
    * Add the following HTML content to the file. This includes the required email address inside the special comments.

3. **Push the File to GitHub**:
    * Initialize a git repository in your local folder, commit the `index.html` file, and push it to the `my-portfolio` repository on GitHub.

    ```bash
    # In your project folder
    git init
    git add index.html
    git commit -m "Add initial portfolio page"
    git branch -M main
    # Replace <USER> with your GitHub username
    git remote add origin https://github.com/<USER>/my-portfolio.git
    git push -u origin main
    ```

4. **Enable GitHub Pages**:
    * Go to your `my-portfolio` repository on GitHub.
    * Click on the "Settings" tab.
    * In the left sidebar, click on "Pages".
    * Under "Build and deployment", for the "Source", select "Deploy from a branch".
    * For the "Branch", select `main` and keep the folder as `/ (root)`. Click "Save".

5. **Get the URL**:
    * After a minute or two, GitHub will build and deploy your site.
    * Refresh the "Pages" settings page. A green banner will appear at the top with your public URL, like `https://<USER>.github.io/my-portfolio/`.
    * Copy this URL for submission.

## 4. Code / Configuration File (`index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <title>My Website</title>
</head>
<body>
<!--email_off-->23f3004197@ds.study.iitm.ac.in<!--/email_off-->
</body>
</html>

````

## 5. How to  Verify

1. Open the public GitHub Pages URL you generated in your browser.
2. You should see the content from your `index.html` file.
3. Right-click on the page and select "View Page Source".
4. Verify that your email `23f3004197@ds.study.iitm.ac.in` is present and correctly wrapped in the `<!--email_off-->` and `<!--/email_off-->` comments.
5. Submit the URL to the exam platform.
