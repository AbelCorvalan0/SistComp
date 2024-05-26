# Import ctypes library
import ctypes

# Carga la libreria (Programa en lenguaje C)
lib= ctypes.CDLL('./main.so')

# Se define los tipos de argumentos de la funcion.
lib.calc.argtypes= (ctypes.c_float,)

# Se define el tipo de retorno de la función
lib.calc.restype= (ctypes.c_int)

# Hace de wrapper para llamar a la función de C
def calc(n):
    return lib.calc(n)