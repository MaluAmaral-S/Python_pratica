for i in range(1, 51, 2):
    print(i)


soma = 0
for i in range(1, 101):
    soma += i

print("A soma de todos os números de 1 a 100 é:", soma)


numero = int(input("Digite um número para ver sua tabuada: "))
print("Tabuada de", numero, ":")
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)

