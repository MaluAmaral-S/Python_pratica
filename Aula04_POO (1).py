class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return print(f'O aluno {self.nome} tem {self.idade} anos')


class Escola:
    def __init__(self, nome, bairro, andares):
        self.nome = nome
        self.bairro = bairro
        self.andares = andares
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)


# Programa Principal
aluno1 = Aluno('Alyson', 17)
aluno2 = Aluno('Rafael', 16)
aluno3 = Aluno('Amanda', 17)

escola = Escola('Polo ICP', 'Monte Serrat', 1)
escola.adicionar_aluno(aluno1)
escola.adicionar_aluno(aluno2)
escola.adicionar_aluno(aluno3)

print(f'A escola de programção {escola.nome} fica no bairro'
      f' {escola.bairro} e o prédio tem {escola.andares} andar(es)')
print(escola.alunos[2].apresentar())
