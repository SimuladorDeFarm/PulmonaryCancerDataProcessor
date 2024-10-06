import numpy as np
import pandas as pd

def estandarizar(matriz):
    # Transponer la matriz para separar variables continuas y binarias
    matriz = np.transpose(matriz)
    
    # Extraer la fila de edades (la segunda fila según tu descripción)
    matrizContinua = matriz[1:2, :]  # Extrae como matriz 2D
    matrizBinaria = np.delete(matriz, 1, axis=0)  # Elimina la fila de edades
    
    # Asegurar que ambas matrices tengan el tipo correcto
    matrizContinua = matrizContinua.astype(float)
    matrizBinaria = matrizBinaria.astype(float)
    
    # Calcular la media y desviación estándar de las variables binarias
    MedBin = np.mean(matrizBinaria, axis=1)    
    DesBin = np.std(matrizBinaria, axis=1)    
    
    # Asegurarse de que los tamaños coincidan
    MedBin = MedBin[:, np.newaxis]
    DesBin = DesBin[:, np.newaxis]
    
    # Estandarizar las variables binarias
    matrizBinEst = (matrizBinaria - MedBin) / DesBin  # Estandarizar fila por fila

    # Calcular el valor mínimo y máximo de la variable continua (edades)
    MedCon = np.min(matrizContinua)
    Descon = np.max(matrizContinua)

    # Normalizar la fila de edades
    matrizConEst = (matrizContinua - MedCon) / Descon

    # Insertar la matriz de edades normalizada de vuelta en la posición original (fila 1)
    matriz_final = np.insert(matrizBinEst, 1, matrizConEst.flatten(), axis=0)

    # Volver a transponer para devolver la matriz a su forma original
    matriz_final = np.transpose(matriz_final)


    #print("media de los datos bin:", MedBin)
    #print("dev estandar de los datos bin:", DesBin)
    
    return matriz_final
