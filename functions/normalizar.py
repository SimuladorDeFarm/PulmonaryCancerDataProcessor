
import numpy as np
import pandas as pd

def normalizar(matriz):
    
    matriz = np.transpose(matriz)
    matrizContinua = matriz[1:2, : ]
    matrizBinaria = np.delete(matriz, 1, axis=0)


    matrizMinBin = np.min(matrizBinaria)    # Valor mínimo en la matriz
    matrizMaxBin = np.max(matrizBinaria)    # Valor máximo en la matriz

    # Normalizar
    matrizBinNor = (matrizBinaria - matrizMinBin) / (matrizMaxBin - matrizMinBin)


    
    matrizMinCon = np.min(matrizContinua)
    matrizMaxCon = np.max(matrizContinua)

    matrizConNor = (matrizContinua - matrizMinCon) / (matrizMaxCon - matrizMinCon)

    matriz_final = np.insert(matrizBinNor, 1, matrizConNor.flatten(), axis=0)

    #print(matrizBinaria)
    
    #print("Matriz original: ",matriz)
    #print("Matriz bin normalizada: ",matrizBinNor)
    #print("Matriz normalizada continuo: ",matrizConNor)
    #print("Matriz final: ", matriz_final)
    #print("numero menor: ", matrizMinCon)
    #print("numero mayor: ", matrizMaxCon)
    matriz_final = np.transpose(matriz_final)
    return matriz_final