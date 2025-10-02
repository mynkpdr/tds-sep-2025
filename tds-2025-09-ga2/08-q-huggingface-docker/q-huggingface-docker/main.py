from fastapi import FastAPI, HTTPException
import os

app = FastAPI()

TOKEN = os.environ.get("GA2_TOKEN_624F", None)


@app.get("/")
def greet():
    return {"Hello": "World!"}


@app.get("/token")
def token():
    if TOKEN:
        return {"success": True, "token": TOKEN[:4]}
    else:
        raise HTTPException(status_code=404, detail="Token not found")
