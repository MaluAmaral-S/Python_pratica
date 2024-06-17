import matplotlib.pyplot as plt
import numpy as np

def plota_pizza_1():
    labels = ['Corinthians', 'Palmeiras', 'Santos', 'São Paulo']
    titulos = [27, 22, 22, 22]
    cores = ['lightblue', 'green', 'white', 'red']
    explode = (0.1, 0, 0, 0)
    total = sum(titulos)
    plt.pie(titulos, explode=explode, labels=labels, colors=cores, autopct=lambda p: '{:.0f}'.format(p * total / 100), shadow=True, startangle=90)

    plt.axis('equal')
    plt.show()

plota_pizza_1()
