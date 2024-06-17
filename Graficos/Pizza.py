import matplotlib.pyplot as plt

A = ['Futebol', 'Volei', 'Luta', 'Natação', 'Basquete']
B = [40, 15, 15, 10, 20]

plt.pie(B, labels=A, autopct='%1.1f%%')
plt.title('Gráfico de Esportes Praticados na Turma')
plt.show()