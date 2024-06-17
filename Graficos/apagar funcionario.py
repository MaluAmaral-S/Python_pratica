import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='clientes'
)

nome = input('Nome do funcionário a ser excluído: ')

cursor = conexao.cursor()

cursor.execute("DELETE FROM funcionários WHERE nome = %s", (nome,))

conexao.commit()

cursor.close()
conexao.close()

print(f"Funcionário {nome} excluído com sucesso!")
