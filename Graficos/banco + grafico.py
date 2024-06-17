import pymysql
import matplotlib.pyplot as plt

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='clientes'
)

cursor = conexao.cursor()

cursor.execute('SELECT * FROM funcionários')
dados = cursor.fetchall()

ids = [info[0] for info in dados]
nomes = [info[1] for info in dados]
salarios = [info[2] for info in dados]

cursor.close()

for info in range (0, 11):
    print(f'{nomes[info]} Salario: {salarios[info]}')


plt.bar(nomes, salarios)
plt.xlabel('Nomes')
plt.ylabel('salarios')
plt.show()
