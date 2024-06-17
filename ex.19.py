def imprimir_chaves_e_valores(dicionario):
    print("Chaves:")
    for chave in dicionario.keys():
        print(chave)

    print("\nValores:")
    for valor in dicionario.values():
        print(valor)

meu_dicionario = {'a': 1, 'b': 2, 'c': 3}
imprimir_chaves_e_valores(meu_dicionario)
