from functions.cargarArchivo    import cargar_archivo
from functions.convertir        import convertir 
from functions.validarDatos     import validarDto
from functions.normalizar       import normalizar
from functions.estandarizar     import estandarizar
from functions.frecEdad         import frecEdad
from functions.outlider         import obtenerOutlider
from functions.outlider         import outliderV2
from functions.medidasTendenciaCentral import medidasTendenciaCentral
from functions.medidasDispercion        import medidasDispercion
from functions.frecuencia       import frecuencia

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

#elimina los outliders de la matriz estandar, normal y original
matrizEstSinOutliders, matrizOrSinOuliders = outliderV2(matrizEst, matriz)
trash, matrizNorSinOuliders =  outliderV2(matrizEst, matrizNor)

#tea de presision al imprimir numpy
np.set_printoptions(threshold=np.inf)
#np.set_printoptions(precision=2, suppress=True)

#obiene medidas de tendencia central
#tendenciaCentral= medidasTendenciaCentral(matrizEstSinOutliders)

#cambia el foramto de impresion 
np.set_printoptions(suppress=True, precision=2)


#medidas de dispercion
medidasDispercion = medidasDispercion(matrizOrSinOuliders)
#print(medidasDispercion)

graficarTodo()