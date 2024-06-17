numero = int(input('diga um numero'))

def par(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar'


resultado = par(numero)
print(resultado)

for i in range(1, 11):
    numero * i
    print(numero, "x", i, "=", numero * i)
