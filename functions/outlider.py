import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import norm
from functions.graficar import graficar 

def outlider(matriz):
    #arreglo_estandarizado = np.transpose(matriz)
    arreglo_estandarizado = matriz[:, 1:2 ]

# Calcular la media y la desviación estándar
    media = np.mean(arreglo_estandarizado)  # Debe ser cercano a 0
    desviacion_estandar = np.std(arreglo_estandarizado)  # Debe ser cercano a 1

    # Definir límites para identificar outliers
    limite_inferior = media - 3 * desviacion_estandar
    limite_superior = media + 3 * desviacion_estandar

    # Identificar outliers
    #outliers = arreglo_estandarizado[(arreglo_estandarizado < limite_inferior) | (arreglo_estandarizado > limite_superior)]
    indices_outliers = np.where((arreglo_estandarizado < limite_inferior) | (arreglo_estandarizado > limite_superior))[0]

    arreglo_sin_outliers = np.delete(arreglo_estandarizado, indices_outliers)

    # Mostrar resultados
    print(f"Arreglo original: {arreglo_estandarizado}")
    print(f"Límite inferior: {limite_inferior}, Límite superior: {limite_superior}")
    print(f"Outliers encontrados en los índices: {indices_outliers}")
    print(f"Arreglo sin outliers: {arreglo_sin_outliers}")

    
