Atualizações nos atalhos do teclado … Em quinta-feira, 1 de agosto de 2024, os atalhos de teclado do Drive serão atualizados para oferecer a navegação por letras iniciais.Saiba mais
Aula07_Histograma.py
import matplotlib.pyplot as plt

A = ['João', 'Maria', 'José', 'Ana']
B = [8.2, 9.3, 10.0, 8.7]

plt.bar(A, B, color='green')
plt.xlabel('Nomes de Alunos')
plt.ylabel('Média das Notas')
plt.title('Histograma Alunos x Média')
plt.show()