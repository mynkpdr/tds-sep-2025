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
