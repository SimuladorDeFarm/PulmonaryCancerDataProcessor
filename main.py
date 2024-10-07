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
import numpy as np
import pandas as pd


matriz = cargar_archivo()

#matriz = np.array([["2", "1", "0"], ["1", "0", "1"]])

# valida los datos de la matriz sino lo elimina
validarDto(matriz)

#convierte genero y diagnostico por 2 y 1
matriz = convertir(matriz)



matrizNormalizada = matriz
matrizNor = normalizar(matriz)

#print("matriz normal:\n",matrizNor)


matrizEst = estandarizar(matriz)
#print("matriz estandar:\n",matrizEst)

#frecEdad(matrizNor)

matrizEstSinOutliders, matrizOrSinOuliders = outliderV2(matrizEst, matriz)
trash, matrizNorSinOuliders =  outliderV2(matrizEst, matrizNor)

#print(matriz)
#print("filas(original, estandar):",matriz.shape[0], matrizEstSinOutliders.shape#[0] )
#print("columnas(original, estandar):", matriz.shape[1], matrizEstSinOutliders.#shape[1] )
np.set_printoptions(threshold=np.inf)

#np.set_printoptions(precision=2, suppress=True)

#tendenciaCentral= medidasTendenciaCentral(matrizEstSinOutliders)

medidasDispercion(matrizOrSinOuliders)

#print("medias:",tendenciaCentral[0])
#print("medianas",tendenciaCentral[1])
#print("modas",tendenciaCentral[2])
#print(matrizNorSinOuliders)

