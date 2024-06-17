import pandas as pd

dados = {
    'Nome': ['Marcos', 'Maria', 'Pedro', 'Amandã'],
    'Idade': [18, 19, 12, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília']
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Exibindo o conteúdo do DataFrame
print(df)
