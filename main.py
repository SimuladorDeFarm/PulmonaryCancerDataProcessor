from functions.cargarArchivo    import cargar_archivo
from functions.convertir        import convertir 
from functions.validarDatos     import validarDto
from functions.normalizar       import normalizar
from functions.estandarizar     import estandarizar
from functions.frecEdad         import frecEdad
from functions.frecEdad         import frec1d
from functions.outlider         import obtenerOutlider
from functions.outlider         import outliderV2
from functions.medidasTendenciaCentral import medidasTendenciaCentral
from functions.medidasDispercion        import medidasDispercion
from functions.frecuencia       import frecuencia
from functions.graficarTodo     import graficarTodo
from functions.graficar         import graficar

import numpy as np
import pandas as pd



#carga el archivo en una matriz numpy
matriz = cargar_archivo()


# valida los datos de la matriz sino lo elimina
validarDto(matriz)

#convierte genero y diagnostico por 2 y 1
matriz = convertir(matriz)


#normaliza matriz original
matrizNormalizada = matriz
matrizNor = normalizar(matriz)

#estadnariza matriz original
matrizEst = estandarizar(matriz)

#print("Posiscion estandarizada de 21 años: ",matrizEst[22][1])
#print("Posiscion estandarizada de 38 años: ", matrizEst[238][1])




#elimina los outliders de la matriz estandar, normal y original
matrizEstSinOutliders, matrizOrSinOuliders = outliderV2(matrizEst, matriz)
trash, matrizNorSinOuliders =  outliderV2(matrizEst, matrizNor)




#tea de presision al imprimir numpy
np.set_printoptions(threshold=np.inf)
#np.set_printoptions(precision=2, suppress=True)

#obiene medidas de tendencia central
#tendenciaCentral= medidasTendenciaCentral(matrizOrSinOuliders)
#print(tendenciaCentral)

#cambia el foramto de impresion 
np.set_printoptions(suppress=True, precision=2)



#medidas de dispercion
medidasDispercion = medidasDispercion(matrizOrSinOuliders)
#print(medidasDispercion)

#genera grafico normal de edades
graficarTodo(matrizOrSinOuliders)
