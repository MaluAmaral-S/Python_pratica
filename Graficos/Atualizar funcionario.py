import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='clientes'
)

salario = int(input('salario '))
nome = str(input('Funcionario '))

cursor = conexao.cursor()

cursor.execute('UPDATE funcionários SET salario = %s WHERE nome = %s', (salario, nome))
conexao.commit()

cursor.close()

print('funcionario atualizado com sucesso!')
