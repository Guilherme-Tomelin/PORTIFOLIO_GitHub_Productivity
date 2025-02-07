import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN_KEY = os.getenv("TOKEN_KEY")
headers = {"Authorization": f"token {TOKEN_KEY}"}

username = "Guilherme-Tomelin"
api_url = f"https://api.github.com/users/{username}"

response = requests.get(api_url, headers=headers)

