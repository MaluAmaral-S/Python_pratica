def uniao_conjuntos(conjunto1, conjunto2):
    uniao = conjunto1 | conjunto2
    return uniao

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
resultado = uniao_conjuntos(conjunto1, conjunto2)
print("União dos conjuntos:", resultado)
