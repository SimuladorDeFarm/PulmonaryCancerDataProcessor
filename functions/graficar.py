import matplotlib.pyplot as plt
from scipy.stats import norm

import numpy as np

def graficar(edad_normalizada, frecuencia):
    # Crear el gráfico de líneas
    plt.plot(edad_normalizada, frecuencia, marker='o', linestyle='-', color='b', label='Frecuencia de edades')

    # Añadir etiquetas y título
    plt.xlabel('Edades normalizadas')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de frecuencias de edades normalizadas')

    # Generar la curva de distribución normal teórica para comparar
    x = np.linspace(0, 1, 100)
    y = norm.pdf(x, 0, 1) * max(frecuencia) / max(norm.pdf(x, 0, 1))  # Escalar la curva para compararla con la frecuencia
    #plt.plot(x, y, color='r', linestyle='--', label='Curva normal teórica')
    plt.axvline(x=0.5, color='red', linestyle='--', linewidth=2, label='x = 0.5')
    
    # Añadir leyenda
    plt.legend()

    # Mostrar el gráfico
    plt.show()