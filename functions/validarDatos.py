import numpy as np
import pandas as pd

def corroboraciones(dato, fila):

    
    error = 0
    
    if fila == 0:
        if dato != "F" and dato != "M":
            print("ERROR: ", dato )
            print(fila)
            error += 1
    if fila == 15:
        if dato != 'YES' and dato != 'NO':
            print("ERROR: ", dato )
            error += 1
    if fila == 1:
        if not isinstance(dato, (int, float)):
            print("ERROR: ", dato )
            error += 1
    if fila != 0 and fila != 15 and fila != 1:
        if dato != 2 and dato != 1:
            print("ERROR: ", dato )
            error += 1
   

def validarDto(matriz):

    matriz = np.transpose(matriz)

    numFilas = matriz.shape[0]
    numColumnas = matriz.shape[1]

    #print(matriz[1][])
    i = 0
    j = 0
    errores = 0
    while i < numFilas:
        j = 0
        while j < numColumnas:
            
            corroboraciones(matriz[i][j], i)
            j += 1
        i += 1
    #print("errores totales: ",errores)
    print("filas:", numFilas)
    print("columnas:", numColumnas)
    #tipo_columna = matriz[:, 1].dtype
    #print(tipo_columna)
    