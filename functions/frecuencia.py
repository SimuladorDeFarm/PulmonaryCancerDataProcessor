import numpy as np
from scipy import stats

def frecuencia(array): 

    # Obtener los valores únicos y sus respectivas frecuencias
    valores_unicos, frecuencias = np.unique(array, return_counts=True)    

    if valores_unicos[0] == 2:
        frecuencias = np.flip(frecuencias)


    #print(valores_unicos, frecuencias)
    return frecuencias, valores_unicos

