import requests

# URL da API do GitHub para buscar informações de um usuário
url = 'https://api.github.com/users/octocat'

# Fazendo a solicitação GET à API
response = requests.get(url)

# Verificando se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Exibindo a resposta da API
    print("Resposta da API:")
    print(response.json())
else:
    print("A solicitação falhou. Código de status:", response.status_code)
