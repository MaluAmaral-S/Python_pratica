import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='clientes'
)

nome = str(input('Informe o nome'))
salario = int(input('Informe o salario '))

cursor = conexao.cursor()

cursor.execute('INSERT INTO funcionários (nome, salario) '
               'VALUES (%s, %s)', (nome, salario))
conexao.commit()

cursor.close()

print('Seu Funcionario foi cadastrado com sucesso')
