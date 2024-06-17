import os

# Solicita ao usuário o caminho do diretório
caminho_diretorio = input("Digite o caminho do diretório: ")

# Verifica se o caminho fornecido é um diretório válido
if os.path.isdir(caminho_diretorio):
    # Lista todos os arquivos no diretório fornecido
    arquivos = os.listdir(caminho_diretorio)

    if arquivos:
        print("Arquivos no diretório:")
        for arquivo in arquivos:
            print(arquivo)
    else:
        print("O diretório está vazio.")
else:
    print("O caminho fornecido não é um diretório válido.")
