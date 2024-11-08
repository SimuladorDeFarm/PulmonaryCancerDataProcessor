import numpy as np
from scipy import stats
from functions.frecuencia import frecuencia

def medidasDispercion(matriz):

    #crea un vector de 5 columnas y 16 filas
    dispercion = np.full((5, 16), 0).astype(float)

    #captura cantidad de columnas
    nColumnas = matriz.shape[1]
    
    #vector = matriz[:, 3:4].astype(float)

    #frecuencia(vector)

    i = 0
    # nColumnas = 16
    while i < nColumnas:
        #toma una linea de la matriz y la vuelve un array
        vector = matriz[:, i:i+1].astype(float)

        if i == 1:  

            media = np.mean(vector)
            desEstandar = np.std(vector)
            varianza = np.var(vector)
            rango = np.max(vector) - np.min(vector)
            coefVar = desEstandar / media
            #print("[EDADES]")
        else: 
            #cacula la frecuencia de los datos binarios en roden [1, 2]
            vector_frecuencia = frecuencia(vector)
            #vector_frecuencia = vector_frecuencia[1]
            media = np.mean(vector_frecuencia)
            desEstandar = np.std(vector_frecuencia)
            varianza = np.var(vector_frecuencia)
            rango = np.max(vector_frecuencia) - np.min(vector_frecuencia)
            coefVar = desEstandar / media
        

        dispercion[0][i] = media
        dispercion[1][i] = desEstandar
        dispercion[2][i] = varianza
        dispercion[3][i] = rango
        dispercion[4][i] = coefVar 

        print(f"Media de las frecuencias: {media:.2f}")
        print(f"Desviación estándar de las frecuencias: {desEstandar:.2f}")
        print(f"Varianza de las frecuencias: {varianza:.2f}")
        print(f"Rango de las frecuencias: {rango}")
        print(f"Coeficiente de variación: {coefVar:.2f}")

        #print(f"Media de las frecuencias: {dispercion[0][i]:.2f}")
        #print(f"Desviación estándar de las frecuencias: {dispercion[1][i]:.2f}")
        #print(f"Varianza de las frecuencias: {dispercion[2][i]:.2f}")
        #print(f"Rango de las frecuencias: {dispercion[3][i]}")
        #print(f"Coeficiente de variación: {dispercion[4][i]:.2f}")
        
        i+=1
    
    return dispercion
    #print(f"Media: {dispercion[:][0]}")
    #print(f"Desviación estándar: {dispercion[:][1]}")
    #print(f"Varianza : {dispercion[:][2]}")
    #print(f"Rango : {dispercion[:][3]}")
    #print(f"Coeficiente de variación: {dispercion[:][4]}")
    #print(f"Frecuencia de '1' en cada columna: {frecuencia_de_1}")

