import numpy as np
import pandas as pd


def cargar_archivo():
    # Leer el archivo Excel en un DataFrame
    nombre_archivo = "lung_cancer_survey.xlsx"
    df = pd.read_excel(nombre_archivo)

    # Convertir el DataFrame en una matriz de numpy
    matriz = df.to_numpy()
    #np.set_printoptions(threshold=np.inf)
    # Imprimir la matriz completa
    #print("Matriz de datos cargada:")
    #print(matriz)
    

    
    return matriz