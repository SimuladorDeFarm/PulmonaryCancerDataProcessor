import numpy as np
import pandas as pd

def validarDto(matriz):

    matriz = np.transpose(matriz)

    numFilas = matriz.shape[0]
    numColumnas = matriz.shape[1]

    #print(matriz[1][])
    i = 2
    j = 0
    errores = 0
    while i < numFilas-1:
        j = 0
        while j < numColumnas:
            
            if matriz[i][j] != 2 and matriz[i][j] != 1: 
                print("error") 
                errores += 1
                print("error: ", matriz[i][j])
                print("i =", i)
                print("j =", j) 
                print("------")
            j += 1
        i += 1
    print("errores totales: ",errores)
    print("filas:", numFilas)
    print("columnas:", numColumnas)
    #tipo_columna = matriz[:, 1].dtype
    #print(tipo_columna)
    