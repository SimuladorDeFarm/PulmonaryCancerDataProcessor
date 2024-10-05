from functions.cargarArchivo    import cargar_archivo
from functions.convertir        import convertir 
from functions.validarDatos import validarDto
import numpy as np
import pandas as pd


matriz = cargar_archivo()

#matriz = np.array([["2", "1", "0"], ["1", "0", "1"]])

# valida los datos de la matriz sino lo elimina
validarDto(matriz)

#convierte genero y diagnostico por 2 y 1
convertir(matriz)
