import matplotlib.pyplot as plt
from random import randint

A = [randint(1, 1000) for _ in range(1000)]
B = [randint(1, 100) for _ in range(1000)]

plt.scatter(A, B)
plt.xlabel('Valores A')
plt.ylabel('Valores B')
plt.title('Gráfico de Dispersão A x B')
plt.show()
