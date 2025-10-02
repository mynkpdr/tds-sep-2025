# 12. FastAPI Google OAuth Login Verification (1.5 marks)

## 1. Problem Description

The goal is to build a FastAPI application that implements a "Sign in with Google" feature using OAuth 2.0 and OpenID Connect. The application should handle the authentication flow, store the user's `id_token` in a server-side session, and expose an endpoint to retrieve it.

## 2. Understanding the Requirements

* **Framework**: FastAPI.
* **Authentication**: Google SSO (OAuth 2.0).
* **User Flow**:
    1. A user visits a login endpoint and is redirected to Google.
    2. After logging in, Google redirects the user back to a callback endpoint in the application.
    3. The application exchanges the authorization code from Google for an `id_token`.
    4. The `id_token` is stored securely in a session.
* **Submission**: You need to log in with your email, retrieve your `id_token`, and submit it along with your Google Client ID as a JSON object:

    ```json
    {
      "id_token": "eyJ...",
      "client_id": "YOUR_CLIENT_ID"
    }
    ```

## 3. Step-by-Step Solution

#### Step 1: Create Google OAuth Credentials

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Navigate to **APIs & Services \> Credentials**.
4. Click **+ CREATE CREDENTIALS** and select **OAuth client ID**.
5. If prompted, configure the "OAuth consent screen". Choose **External** and provide an app name, user support email, and developer contact information.
6. For the **Application type**, select **Web application**.
7. Under **Authorized redirect URIs**, add `http://127.0.0.1:8000/auth`. This is the callback URL your FastAPI app will use.
8. Click **CREATE**. You will be given a **Client ID** and a **Client Secret**. Copy these values.

#### Step 2: Set Up the FastAPI Project

1. Create a project folder. Inside it, create `main.py`, `requirements.txt`, and a `.env` file.
2. In the `.env` file, store your credentials:

    ```bash
    GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
    GOOGLE_CLIENT_SECRET=your-gcp-client-secret
    # A random string for session encryption
    SECRET_KEY=my-super-secret-string-for-sessions
    ```

3. Populate `main.py` and `requirements.txt` with the code below.

#### Step 3: Run the Application and Log In

1. Install dependencies: `pip install -r requirements.txt`.
2. Run the server: `uvicorn main:app --reload`.
3. Open your browser and go to `http://127.0.0.1:8000/login`.
4. You will be redirected to the Google login page. **Log in using the email `23f3004197@ds.study.iitm.ac.in`**.
5. After successful login, you will be redirected back to `http://127.0.0.1:8000/`.

#### Step 4: Retrieve the Token and Client ID

1. After logging in, navigate to `http://127.0.0.1:8000/id_token`.
2. The browser will display the required JSON object containing your `id_token` and `client_id`.
3. Copy this entire JSON object and paste it into the answer field on the exam page.

## 4. Code / Configuration Files

#### `.env`

```
GOOGLE_CLIENT_ID=PASTE_YOUR_CLIENT_ID_HERE
GOOGLE_CLIENT_SECRET=PASTE_YOUR_CLIENT_SECRET_HERE
SECRET_KEY=GENERATE_A_RANDOM_SECRET_KEY_HERE
```

#### `requirements.txt`

```
fastapi
uvicorn
python-dotenv
Authlib
itsdangerous
httpx
```

#### `main.py`

```python
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Add session middleware to handle user sessions
# The secret key is used to sign the session cookie
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY"))

# Configure Authlib's OAuth client
oauth = OAuth()
oauth.register(
    name="google",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)


@app.get("/")
async def homepage(request: Request):
    user = request.session.get("user")
    if user:
        return HTMLResponse(
            f'<h1>Hello, {user["email"]}!</h1><p><a href="/id_token">Get Token</a></p><p><a href="/logout">Logout</a></p>'
        )
    return HTMLResponse(
        '<h1>Welcome!</h1><p><a href="/login">Login with Google</a></p>'
    )


@app.get("/login")
async def login(request: Request):
    # The redirect_uri must match one of the URIs configured in the Google Cloud Console
    redirect_uri = request.url_for("auth")
    return await oauth.google.authorize_redirect(request, redirect_uri)


@app.get("/auth")
async def auth(request: Request):
    # Handle the callback from Google
    token = await oauth.google.authorize_access_token(request)
    # The user info is available in the 'userinfo' field of the token
    user = token.get("userinfo")
    if user:
        # Store user info and the id_token in the session
        request.session["user"] = dict(user)
        request.session["id_token"] = token.get("id_token")
    return RedirectResponse(url="/")


@app.get("/logout")
async def logout(request: Request):
    # Clear the session
    request.session.pop("user", None)
    request.session.pop("id_token", None)
    return RedirectResponse(url="/")


@app.get("/id_token", response_class=JSONResponse)
async def get_id_token(request: Request):
    # Endpoint to retrieve the required data for submission
    id_token = request.session.get("id_token")
    if not id_token:
        return {"error": "User not logged in or token not found."}

    # Prepare the JSON object for submission
    submission_data = {"id_token": id_token, "client_id": os.getenv("GOOGLE_CLIENT_ID")}
    return submission_data
```
