import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

from functions.graficar import graficar
from functions.frecuencia import frecuencia

def nombreEjey(numero):

    if numero == 0:
        return "Genero"
    if numero == 1:
        return "Edad"
    if numero == 2:
        return "Fumar"
    if numero == 3:
        return "Dedos amarillos"
    if numero == 4:
        return "Anciedad"
    if numero == 5:
        return "Presion social"
    if numero == 6:
        return "Enfermedad cronica"
    if numero == 7:
        return "Fatiga"
    if numero == 8:
        return "alergia"
    if numero == 9:
        return "consumo de alcohol"
    if numero == 10:
        return "Tos"
    if numero == 11:
        return "dificultad para respirar"
    if numero == 12:
        return "Dificultad para tragar"
    if numero == 13:
        return "Dolor de pecho"
    if numero == 14:
        return "Deds amarillos"
    if numero == 15:
        return "Cancer de pulmon"
    
def frecedades(vector):
    return np.unique(vector, return_counts=True)


 
    
    

def graficarTodo(matriz):
    i = 0
    nColumnas = matriz.shape[1]

    while i <   nColumnas :
        vector = matriz[:, i].astype(int)

        if i != 1:
            
            # [1, 2]
            vector_fre, valores_unicos = frecuencia(vector)
            #print(vector_fre, valores_unicos)
            #print(vector_fre, valores_unicos)
            plt.bar(valores_unicos, vector_fre, color=['blue', 'orange'], width=0.4)

            plt.xticks(valores_unicos, ['No', 'si'])
            # Añadir etiquetas
            plt.xlabel(nombreEjey(i))
            plt.ylabel("Frecuencia")
            plt.title(f'Frecuencia vs {nombreEjey(i)}')
            #plt.xticks(valores_binarios)  # Etiquetas para los valores en el eje x

            # Mostrar la gráfica
            #plt.show()
            #plt.savefig(f"graficos/{nombreEjey(i)}")
        else:
            print(vector)
            vector_fre, valores_unicos = frecedades(vector)
            #matriz_comb = np.column_stack((valores_unicos, vector_fre))
            #graficar(matriz_comb)
            print( frecedades)
        i+=1