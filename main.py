import os
import requests
from dotenv import load_dotenv

load_dotenv()


TOKEN_KEY = os.getenv("TOKEN_KEY")
headers = {"Authorization": f"token {TOKEN_KEY}"}

username = "Guilherme-Tomelin"
api_url = f"https://api.github.com/users/{username}"

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(f"Nome de usuário: {data['login']}")
    print(f"Repositórios públicos: {data['public_repos']}")
    print(f"Seguidores: {data['followers']}")
    print(f"Seguindo: {data['following']}")
else:
    print("Erro ao obter dados do usuário.")
