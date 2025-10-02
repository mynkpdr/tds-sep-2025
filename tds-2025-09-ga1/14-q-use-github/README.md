# 14. Use GitHub (0.5 Marks)

Objective
---------

Demonstrate your ability to use Git and GitHub by creating a repository, committing a specific file, and providing a public URL to that file.

Steps to Get the Answer
-----------------------

## Step 1: Create a GitHub Account

1. Visit [GitHub.com](https://github.com)
2. Click "Sign up" in the top-right corner
3. Enter your:
   - Email address
   - Password (make it strong and secure)
   - Username (this will be your GitHub username)
4. Verify your email address when prompted
5. Complete any additional verification steps if required

## Step 2: Create a New Repository

### Method 1: Through Web Interface (Recommended for Beginners)

1. Click the "+" icon in the top-right corner
2. Select "New repository"
3. Fill in the details:
   - Repository name (e.g., "email-verification")
   - Description (optional)
   - Make it "Public"
   - Check "Add a README file"
4. Click "Create repository"

### Create email.json File (Web Interface)

1. In your new repository:
   - Click "Add file"
   - Select "Create new file"
2. Name it `email.json`
3. Add the following content:

```json
{
    "email": "ROLLNUMBER@ds.study.iitm.ac.in"
}
```

4. At the bottom, add a commit message like "Add email.json"
5. Click "Commit new file"

## Step 3: Get the Raw URL

1. Navigate to your `email.json` file in the repository
2. Click the "Raw" button (or click the file and then click "Raw")
3. Copy the URL - it should look like:

```
https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/REPOSITORY_NAME/main/email.json
```

## Alternative Method: Using Terminal (Advanced)

If you prefer using the terminal:

1. First-time Git setup:

```bash
git config --global user.name "Your Name"
git config --global user.email "ROLLNUMBER@ds.study.iitm.ac.in"
```

2. Clone and create repository:

```bash
git clone https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git
cd REPOSITORY_NAME
```

3. Create email.json:

```bash
echo '{"email": "ROLLNUMBER@ds.study.iitm.ac.in"}' > email.json
```

4. Push to GitHub:

```bash
git add email.json
git commit -m "Add email.json"
git push origin main
```

## Important Notes

- Make sure the repository is **public** so we can verify your submission
- Double-check that your email address is correct in the JSON file
- The raw URL should start with `https://raw.githubusercontent.com/`
- Keep your repository clean - it should only contain `README.md` and `email.json`

## Submission

Submit the raw URL of your email.json file. It should look like:

```
https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/REPOSITORY_NAME/main/email.json
```

## Troubleshooting

- If you get authentication errors in terminal:
  - Use GitHub CLI: `gh auth login`
  - Or generate a Personal Access Token from GitHub Settings → Developer Settings → Personal Access Tokens
- If files aren't showing up:
  - Make sure you committed and pushed your changes
  - Check if you're in the correct repository and branch
- If the raw URL doesn't work:
  - Ensure the repository is public
  - Wait a few minutes for GitHub to process the changes
