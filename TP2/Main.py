from numpy import void
import requests
import ctypes

# Lista de códigos ISO de países latinoamericanos
countries = ['ARG', 'BRA', 'CHL', 'COL', 'MEX', 'PER', 'VEN']

# Mostrar lista de países al usuario
def countriesList():
    return countries

# Solicitar al usuario que ingrese el código de país
#def selectedCountry(country):
    #selecCountry= country
    #return 0
#selected_country = input("Ingrese el código del país que desea consultar: ")

# Verificar si el código de país ingresado es válido
def selectedCountry(country):
    #selectCountry= country
    #return void
    if country in countries:
# Hacer la solicitud para el país seleccionado
     url = f'https://api.worldbank.org/v2/en/country/{selectedCountry}/indicator/SI.POV.GINI?format=json&date=2011:2020'
     response = requests.get(url)
     return response
    else:
     return 0

#     if response.status_code == 200:
#         data = response.json()
        
#         gini_data = {entry['date']: entry['value'] for entry in data[1] if entry['value'] is not None}

#         print(f'Datos para {selected_country}:')
#         print("Años disponibles:")
#         for year in gini_data.keys():  # Modificado para imprimir solo los años con datos disponibles
#             print(year)
        
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