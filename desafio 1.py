#importar uma função da biblioteca
from random import randint

aleatorio = randint(1, 10)

while True:
    resposta = int(input('escreva um numero'))
    if resposta == aleatorio:
        print('vc acertou!')
        print(aleatorio)
        break

    else:
        print('vc errou')
        if resposta < aleatorio:





            print('o numero é maior')
        elif resposta > aleatorio:
            print('o numero é menor')
        print('vc errou')

#renomear biblioteca e importar tudo
import  math as ma
print(ma.pi)
#fazer as funçoes da biblioteca serem como se fossem suas funções
#from math import *
#print(pow(2, 4))
