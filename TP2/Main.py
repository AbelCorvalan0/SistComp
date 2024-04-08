from numpy import void
import requests
import ctypes

#Lista de códigos ISO de países latinoamericanos
countries = ['ARG', 'BRA', 'CHL', 'COL', 'MEX', 'PER', 'VEN']

#Mostrar lista de países al usuario.
def countriesList():
    return countries


#Mostrar lista de años para cada país.

#Verificar si el código de país ingresado es válido
def selectedCountry(country):
    if country in countries:
     # Hacer la solicitud para el país seleccionado
     url= f'https://api.worldbank.org/v2/en/country/{country}/indicator/SI.POV.GINI?format=json&date=2011:2020'
     response= requests.get(url)
     if response.status_code == 200:
        #Llamo a función que ordena y procesa los datos. (Tener en cuenta response.json())
        data= response.json()
        #selectedDate(data)
        return selectedDate(data)
    else:
     return 404

def selectedDate(data):
    gini_data= {entry['date']: entry['value'] for entry in data[1] if entry['value'] is not None}
    #for year in gini_data.keys():  # Modificado para imprimir solo los años con datos disponibles
     #years= "".join(str(list(gini_data)))
    return list(gini_data.keys())

#def processData(response):
#def

#         # Solicitar al usuario que ingrese el año que desea consultar
#         selected_year = input("Ingrese el año que desea consultar: ")  # Modificado para mantener la entrada como una cadena
#         if selected_year in gini_data.keys():
#             # Guardar el índice GINI correspondiente al año seleccionado en la variable gini
#             gini = gini_data[selected_year]
#             print(f'Índice GINI para {selected_year}: {gini}')
#         else:
#             print("Año no disponible para el país seleccionado.")
#     else:
#         print(f'Error al obtener los datos para {selected_country}:', response.status_code)
# else:
#     print("Código de país no válido.")

# #Cargo la biblioteca compartida
# lib = ctypes.CDLL('./main.so')

# # Defino el tipo de argumento y el tipo de retorno de la función
# lib.cFloatToInt.argtypes = [ctypes.c_float]
# lib.cFloatToInt.restype = ctypes.c_int
# value_to_convert = lib.cFloatToInt(ctypes.c_float(gini))
# print(f'Valor entero obtenido: {value_to_convert}')