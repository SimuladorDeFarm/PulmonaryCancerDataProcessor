import numpy as np
from functions.graficar import graficar 

def frec1d(arreglo):
    
    
    valores_unicos, conteos = np.unique(arreglo, return_counts=True)

    # Crear un arreglo de frecuencias como una tupla de (valor, frecuencia)
    frecuencias = np.column_stack((valores_unicos, conteos))

    # Ordenar el arreglo de frecuencias por el primer elemento (valor)
    frecuencias = frecuencias[frecuencias[:, 0].argsort()]
     


    return frecuencias

def frecEdad(matriz):

    matriz = np.transpose(matriz)
    matrizNorEdad = matriz[1:2, :]
    #print(matrizNorEdad)

    #matrizOr = np.transpose(matrizOr)
    #edadMenor = matrizOr[1:2, :]
    #j = np.sort(edadMenor)
    #print(j)
    
    vector_ordenado = np.sort(matrizNorEdad)
    #print(vector_ordenado)


    edades, frecuencias = np.unique(matrizNorEdad, return_counts=True)
    
    for edad, frecuencia in zip(edades, frecuencias):
        print(f"Edad: {edad}, Frecuencia: {frecuencia}")

    media = np.mean(matrizNorEdad)
    desviacion_estandar = np.std(matrizNorEdad)

    #print(media)
    #print(desviacion_estandar)

    edadesOut = np.delete(edades, 0)
    frecuenciasOut = np.delete(frecuencias, 0)
    graficar(edad, frecuencia)
    #graficar(edadesOut, frecuenciasOut)

    