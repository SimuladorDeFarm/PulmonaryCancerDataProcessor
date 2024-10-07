import numpy as np
from scipy import stats

def medidasTendenciaCentral(matriz):

    
    nColumnas = matriz.shape[1]

    media = -1
    mediana = -1
    i = 0
    tendenciaCentral = np.full((3, 16), -1).astype(float)

    while i < nColumnas:
        
        vector = matriz[:, i:i+1].astype(float)
        # Calcular la moda
        moda = stats.mode(vector, keepdims=True)[0][0]
        tendenciaCentral[2][i] = moda
        media = -1
        mediana = -1
    
        
        if i == 1:
            
            # Calcular la media
            media = np.mean(vector)
            tendenciaCentral[0][i] = media

            # Calcular la mediana
            mediana = np.median(vector)
            tendenciaCentral[1][i] = mediana
        i+=1


        # Mostrar resultados
        #print(f"Media: {media}")
        #print(f"Mediana: {mediana}")
        print(f"Moda: {moda}")
        np.set_printoptions(precision=2, suppress=True)

    return tendenciaCentral