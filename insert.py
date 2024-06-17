import pymysql

conexao = pymysql.connect (
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'Turma_2_Programacao'
)

nome = str(input('Informe o nome do jogo: '))
ano = int(input('Informe o ano de lançamento: '))
preco = float(input('Informe o preco do jogo: '))

cursor = conexao.cursor()

cursor.execute('INSERT INTO Atividade (Jogo, AnodeLancamento, Preco) '
               'VALUES (%s, %s, %s)', (nome, ano, preco))
conexao.commit()

cursor.close()

print('Seu jogo foi cadastrado com sucesso')