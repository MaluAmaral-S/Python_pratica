print('vsf marcos querido <3') # print
nome = 'malu linda' #variavel
print(nome)
dia = 'segunda'
data = 3
print(f'hoje é {dia} dia {data}') #concatenação
''' comentarios em varias linhas '''
Nome = str(input('qual o seu nome?'))
n1 = int(input('digite o primeiro valor'))
n2 = int(input('segundo numero'))
print(Nome)
print(n1 + n2)
'''
 + adição
* multiplicação
/ divisão 
// divisão inteira
** potencia
% resto da divisão impar ou par
'''
idade = int(input('idade?'))
if idade <= 18:
    print('menor de idade')
''' 
< menor
> maior
!= diferente
'''


num = int(input('digite um numero'))

def par(num):
    if num % 2 == 0:
        return 'par'

    else:
        return "impar"


resultado = par(num)
print(f'O numero {num} é {resultado}')
