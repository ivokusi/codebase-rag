from flask import Flask, redirect, request, jsonify
from dotenv import load_dotenv
import requests
import os

load_dotenv()

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

GITHUB_BASE_URL = "https://github.com/login/oauth"
GITHUB_API_URL = "https://api.github.com"

app = Flask(__name__)

@app.route("/github/auth")
def auth():
    """Home route that redirects users to GitHub for authentication."""
    print("Redirecting to GitHub for authentication...")
    auth_url = f"{GITHUB_BASE_URL}/authorize?client_id={GITHUB_CLIENT_ID}&scope=repo"
    return jsonify({"auth_url": auth_url}), 200

@app.route("/github/callback")
def callback():
    """Handles the GitHub callback with the authorization code."""
    code = request.args.get("code")
    if not code:
        return "Error: No authorization code provided", 400

    # Exchange authorization code for access token
    token_url = f"{GITHUB_BASE_URL}/access_token"
    headers = {"Accept": "application/json"}
    data = {
        "client_id": GITHUB_CLIENT_ID,
        "client_secret": GITHUB_CLIENT_SECRET,
        "code": code,
    }

    token_response = requests.post(token_url, headers=headers, data=data)
    token_json = token_response.json()
    access_token = token_json.get("access_token")

    if not access_token:
        return f"Error: {token_json.get('error_description', 'Failed to get access token')}", 400

    # Fetch user repositories
    user_repos_url = f"{GITHUB_API_URL}/user/repos"
    headers = {"Authorization": f"Bearer {access_token}"}
    repos_response = requests.get(user_repos_url, headers=headers)

    if repos_response.status_code != 200:
        return f"Error fetching repositories: {repos_response.json()}", 400

    repos = repos_response.json()
    repos = {repo["name"]: repo["clone_url"] for repo in repos}

    return jsonify(repos), 200

if __name__ == "__main__":
    app.run("0.0.0.0", port=8000)