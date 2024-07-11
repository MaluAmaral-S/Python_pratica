class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f'Meu nome é {self.nome} e tenho {self.idade} anos'  # Utilizando f-string para formatação

class Escola:
    def __init__(self, nome, bairro):
        self.nome = nome
        self.bairro = bairro
        self.alunos = []

    def adicionarAluno(self, aluno):  # Renomeando o método para adicionar um único aluno
        self.alunos.append(aluno)

# Adicionando os alunos à escola
aluno1 = Aluno('Malu', 19)  # Corrigindo o nome do aluno
aluno2 = Aluno('Marcos', 18)  # Corrigindo o nome do aluno
escola = Escola('Escola AB', 'Jardim América')  # Corrigindo o nome da escola
escola.adicionarAluno(aluno1)  # Adicionando aluno1 à escola
escola.adicionarAluno(aluno2)  # Adicionando aluno2 à escola

# Iterando sobre os alunos na escola e apresentando cada um
for aluno in escola.alunos:
    print(aluno.apresentar())

#mostrar isolado
print(escola.alunos[0].apresentar())

