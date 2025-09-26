# /// script
# dependencies = ["python-dotenv", "fastapi", "uvicorn", "httpx"]
# ///

from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse, JSONResponse
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8000/"

@app.get("/login")
def login():
    # Redirect to Google OAuth login
    google_auth_url = (
        "https://accounts.google.com/o/oauth2/v2/auth"
        "?response_type=code"
        f"&client_id={GOOGLE_CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        "&scope=openid%20email%20profile"
        "&access_type=offline"
    )
    return RedirectResponse(url=google_auth_url)

@app.get("/")
def auth_callback(response: Response, code: str = None):
    if not code:
        return JSONResponse({"error": "No code in request"}, status_code=400)

    # Exchange code for tokens
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    token_response = httpx.post(token_url, data=data).json()
    id_token = token_response.get("id_token")

    if not id_token:
        return JSONResponse({"error": "Failed to get id_token"}, status_code=400)

    # Store id_token in a secure HTTP-only cookie
    response = RedirectResponse(url="/dashboard")
    response.set_cookie(
        key="id_token",
        value=id_token,
        httponly=True,  # prevents JS from reading it
        secure=False,   # set True if using HTTPS
        max_age=3600    # expires in 1 hour
    )
    return response

@app.get("/dashboard")
def dashboard(request: Request):
    id_token = request.cookies.get("id_token")
    if not id_token:
        return RedirectResponse(url="/login")
    return JSONResponse({"id_token": id_token, "client_id": GOOGLE_CLIENT_ID})

@app.get("/id_token")
def get_id_token(request: Request):
    id_token = request.cookies.get("id_token")
    if not id_token:
        return JSONResponse({"error": "Not logged in"}, status_code=401)
    return JSONResponse({"id_token": id_token})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)