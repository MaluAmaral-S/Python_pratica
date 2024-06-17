import matplotlib.pyplot as plt

A = [2, 4, 5, 7, 8, 10]
B = [5, 2, 3, 1, 8, 12]

plt.plot(A, B, color='red', linestyle='--', marker='o')
plt.xlabel('Tempo (s)')
plt.ylabel('Quantidade')
plt.title('Gráfico Tempo x Quantidade')
plt.grid()
plt.show()