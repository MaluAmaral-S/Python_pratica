import pymysql
import matplotlib.pyplot as plt

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'clientes'
)

cursor = conexao.cursor()

cursor.execute('SELECT * FROM clientes')
dados = cursor.fetchall(

)

cursor.close()

ids = [dado[0] for dado in dados]
nomes = [dado[1] for dado in dados]
senha = [dado[2] for dado in dados]
email = [dado[3] for dado in dados]
idade = [dado[4] for dado in dados]

print(ids)
print(nomes)
print(senha)
print(email)
print(idade)
#mostrar um indice um embaixo do outro
for nome in nomes:
    print(nome)


plt.bar(nomes, email)
plt.show()
