import pandas as pd
import numpy as np


def convertir(matriz):
    i = 0
    j = 0
    num_filas = matriz.shape[0]
    num_columnas = matriz.shape[1]
   # Recorrer cada fila de la matriz
    while i < num_filas:
        j = 0
        # Recorrer cada columna de la fila actual
        while j < num_columnas:
            #matriz[i][0] = 1  # Asignar el valor 1 a cada elemento
            if matriz[i][0] == 'F':
                matriz[i][0] = 2
            if matriz[i][0] == 'M':
                matriz[i][0] = 1
            
            if matriz[i][15] == 'YES':
                matriz[i][15] = 2
            if matriz[i][15] == 'NO':
                matriz[i][15] = 1
            
            
            j += 1  # Incrementar columna
        i += 1  # Incrementar fila

    #print(matriz)
    return matriz