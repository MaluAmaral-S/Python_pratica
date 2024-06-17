class Livros:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.livros = []
    def descricao(self):
        return f'Livro: {self.titulo}'

self.livros.append(livro)
self.livros.append(livro)

livro1 = Livros('Cem Anos de Solidão', 'Gabriel García Márquez ', 368)
livro2 = Livros(1984, "George Orwell", 328)

print(livro1.descricao())
print(livro2.descricao())

escolha = print(input('Livro 1 ou Livro 2?'))

if escolha == 1:
    print(f'Autor')


