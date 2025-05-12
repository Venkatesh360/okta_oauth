"""
Google OAuth2 Authentication with FastAPI

This module provides endpoints for:
1. Health check ("/")
2. Redirecting users to Google's OAuth2 login
3. Handling the callback from Google and retrieving user information

Dependencies:
- FastAPI
- Requests
- Motor (Async MongoDB client)
"""

from fastapi import FastAPI
import requests

app = FastAPI()

# Replace with actual values from your Google Cloud OAuth2 credentials
CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"
REDIRECT_URI = "http://localhost:8000/auth/callback"

@app.get("/")
def home():
    """
    Health check endpoint.
    
    Returns:
        dict: A simple ping response to confirm the server is running.
    """
    return {"ping": "pong"}

@app.get("/login/google")
async def login_google():
    """
    Generates a Google OAuth2 login URL and returns it to the client.
    
    Returns:
        dict: A dictionary containing the OAuth2 URL.
    """
    url = (
        "https://accounts.google.com/o/oauth2/auth"
        f"?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope=openid%20profile%20email"
        f"&access_type=offline"
    )
    return {"url": url}

@app.get("/auth/callback")
async def auth_google(code: str):
    """
    Callback endpoint to handle Google's response after user authentication.
    
    Args:
        code (str): Authorization code returned by Google after successful login.
    
    Returns:
        dict: User information or error details if the token exchange fails.
    """
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "code": code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    # Exchange authorization code for access token
    response = requests.post(token_url, data=data)
    token_data = response.json()

    if "access_token" not in token_data:
        return {"error": "Token exchange failed", "details": token_data}

    # Use access token to fetch user info
    access_token = token_data["access_token"]
    user_info_response = requests.get(
        "https://www.googleapis.com/oauth2/v1/userinfo",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    user = user_info_response.json()

    return {"user": user}
