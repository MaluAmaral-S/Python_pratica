import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='clientes'
)
def inserir():
    nome = str(input('Informe o nome'))
    salario = int(input('Informe o salario '))

    cursor = conexao.cursor()

    cursor.execute('INSERT INTO funcionários (nome, salario) '
                   'VALUES (%s, %s)', (nome, salario))
    conexao.commit()

    cursor.close()

    print('Seu Funcionario foi cadastrado com sucesso')


def update():
    salario = int(input('salario '))
    nome = str(input('Funcionario '))

    cursor = conexao.cursor()

    cursor.execute('UPDATE funcionários SET salario = %s WHERE nome = %s', (salario, nome))
    conexao.commit()

    cursor.close()

    print('funcionario atualizado com sucesso!')


def delete():
    nome = input('Nome do funcionário a ser excluído: ')

    cursor = conexao.cursor()

    cursor.execute("DELETE FROM funcionários WHERE nome = %s", (nome,))

    conexao.commit()

    cursor.close()
    conexao.close()

    print(f"Funcionário {nome} excluído com sucesso!")


def select():
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM funcionários')
    dados = cursor.fetchall()

    ids = [info[0] for info in dados]
    nomes = [info[1] for info in dados]
    salarios = [info[2] for info in dados]

    cursor.close()

    print(nomes)


escolha = int(input('INSERIR [1] UPDATE[2] DELETE[3] SELECT[4]'))

if escolha == 1:
    inserir()

elif escolha == 2:
    update()

elif escolha == 3:
    delete()

elif escolha == 4:
    select()



