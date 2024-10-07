import matplotlib.pyplot as plt
from scipy.stats import norm

import numpy as np

def graficar(vector):

    Y = vector[:, 1]
    X = vector[:, 0]
    # Crear el gráfico de líneas
    
    
    #X = X[:, np.newaxis]
    #Y = Y[:, np.newaxis]
    
    plt.plot(X, Y, marker='o', linestyle='-', color='b', label='Y de edades')

    # Añadir etiquetas y título
    plt.xlabel('x')
    plt.ylabel('Y')
    plt.title('y vs x')

    # Generar la curva de distribución normal teórica para comparar
    x = np.linspace(0, 1, 100)
    y = norm.pdf(x, 0, 1) * max(Y) / max(norm.pdf(x, 0, 1))  # Escalar la curva para compararla con la Y
    #plt.plot(x, y, color='r', linestyle='--', label='Curva normal teórica')
    plt.axvline(x=0.5, color='red', linestyle='--', linewidth=2, label='x = 0.5')
    
    # Añadir leyenda
    plt.legend()

    # Mostrar el gráfico
    plt.show()