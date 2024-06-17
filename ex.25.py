import json

# Definindo um JSON simples como uma string
json_string = '{"nome": "Malu", "idade": 19, "cidade": "Itaguai"}'

# Carregando o JSON em um objeto Python
objeto_python = json.loads(json_string)

# Exibindo o conteúdo do objeto Python
print("Conteúdo do objeto Python:")
print(objeto_python)
