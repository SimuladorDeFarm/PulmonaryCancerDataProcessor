import numpy as np
import pandas as pd

'''
Modulo creado para probar el codigo de calcular matriz estadnar es correcta

para poder corroborar el resultado creamos un vector pequeño con el que podamos
calcular manualmente la deviacion estandar y la media.

se ingresa una matriz 2x4 y se sacan sus respectivas medias y desviaciones
de cada final, siento estos los resultados

media fila 0: {1,2,3,4} = (1+2+3+4)/4 = 2.5
media fila 1: {5,6,7,8} = (5+6+7+8)/4 = 6.5

dev estandar fila 0: 1.1180339887499
dev estandar fila 1: 1.1180339887499

usamos los datos anteriores para calular la estandarizacion 
fila 0, columna 0: 1

(1 - 2.5)/ 1.1180339887499 = -1.3416 correcto

matriz estandarizda: 
[[-1.34164079 -0.4472136   0.4472136   1.34164079]
 [-1.34164079 -0.4472136   0.4472136   1.34164079]]


'''

def test(matriz):

    med = np.mean(matriz, axis = 1)
    std = np.std(matriz, axis = 1)

    med = med[:, np.newaxis]
    std = std[:, np.newaxis]

    matrizEs = (matriz - med)/ std

    print("desv estandar:", std)
    print("matriz estandarizda:",matrizEs)



array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#print(array[1][1]) #imprime 6

test(array)