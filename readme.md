# FastAPI Google OAuth2 Authentication

This project demonstrates how to integrate **Google OAuth2 login** into a FastAPI backend. It includes endpoints for initiating the login, handling the OAuth2 callback, and fetching authenticated user information.

---

## 🚀 Features

- Google OAuth2 login flow
- Token exchange and user info retrieval
- Asynchronous support with FastAPI

---

## 🧰 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — Modern, fast web framework
- [Requests](https://docs.python-requests.org/en/latest/) — For HTTP requests

---

## 📂 Endpoints

| Method | Endpoint             | Description                                     |
|--------|----------------------|-------------------------------------------------|
| GET    | `/`                  | Health check                                    |
| GET    | `/login/google`      | Generates Google OAuth2 login URL               |
| GET    | `/auth/callback`     | Handles OAuth2 callback and returns user info   |

---

## 🔐 Setup Google OAuth2 Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project → Enable **OAuth2 Consent Screen**
3. Create OAuth 2.0 Client ID credentials:
    - Application type: **Web application**
    - Authorized redirect URI: `http://localhost:8000/auth/callback`
4. Copy your **Client ID** and **Client Secret**

---

## ⚙️ Configuration

Replace the placeholder values in `main.py`:

```python
CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"
REDIRECT_URI = "http://localhost:8000/auth/callback"
TOKEN_URI= "https://oauth2.googleapis.com/token"
```

---

## 🛠 Installation & Running

```bash
# 1. Clone the repo
git clone https://github.com/your-username/fastapi-google-oauth2.git
cd fastapi-google-oauth2

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install fastapi uvicorn requests 

# 4. Run the server
uvicorn main:app --reload
```

---

## ✅ Example Response

After successful login and redirection:

```json
{
  "user": {
    "id": "1234567890",
    "email": "user@example.com",
    "name": "John Doe",
    "picture": "https://example.com/photo.jpg"
  }
}