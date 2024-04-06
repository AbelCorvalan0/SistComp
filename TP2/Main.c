#include <stdio.h>
#include <stdlib.h>

int cFloatToInt(float gini){
    int i_gini = (int) (gini*100)+1;
    return i_gini;
};


#Cargo la biblioteca compartida
lib = ctypes.CDLL('./main.so')

# Defino el tipo de argumento y el tipo de retorno de la función
lib.cFloatToInt.argtypes = [ctypes.c_float]
lib.cFloatToInt.restype = ctypes.c_int
value_to_convert = lib.cFloatToInt(ctypes.c_float(gini))
print(f'Valor entero obtenido: {value_to_convert}')


