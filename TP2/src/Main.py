import requests
import ctypes

# Lista de códigos ISO de países latinoamericanos
countries = ['ARG', 'BRA', 'CHL', 'COL', 'MEX', 'PER', 'VEN']

# Lista de 
listYear= {}
resp= ""
# Mostrar lista de países al usuario
def listaPaises():
#print("Lista de países latinoamericanos:")
    return countries

# Solicitar al usuario que ingrese el código de país
#selected_country = input("Ingrese el código del país que desea consultar: ")
def getDatos(selected_country):
    # Verificar si el código de país ingresado es válido
    if selected_country in countries:
        # Hacer la solicitud para el país seleccionado
        url = f'https://api.worldbank.org/v2/en/country/{selected_country}/indicator/SI.POV.GINI?format=json&date=2011:2020'
        response = requests.get(url)
        resp= response.status_code
        if response.status_code == 200:
            data = response.json()
            #print(data)
            gini_data = {entry['date']: entry['value'] for entry in data[1] if entry['value'] is not None}
        
            print(f'Datos para {selected_country}:')
            print("Años disponibles:")

    return list(gini_data.keys())

def getGINI(selected_country, selected_year):
    # Verificar si el código de país ingresado es válido
    if selected_country in countries:
        # Hacer la solicitud para el país seleccionado
        url = f'https://api.worldbank.org/v2/en/country/{selected_country}/indicator/SI.POV.GINI?format=json&date=2011:2020'
        response = requests.get(url)
        resp= response.status_code
        if response.status_code == 200:
            data = response.json()
            #print(data)
            gini_data = {entry['date']: entry['value'] for entry in data[1] if entry['value'] is not None}
        
    # for year in gini_data.keys():  # Modificado para imprimir solo los años con datos disponibles
    #     print(year)
    #i=0
    # Solicitar al usuario que ingrese el año que desea consultar
    #selected_year = input("Ingrese el año que desea consultar: ")  # Modificado para mantener la entrada como una cadena
    if selected_year in gini_data.keys():
    # Guardar el índice GINI correspondiente al año seleccionado en la variable gini
        gini = gini_data[selected_year]
        #listYear.extend({gini_data[selected_year]})
        #i+=1
        #print(listYear)
        #print(f'Índice GINI para {selected_year}: {gini}')
        return f'Índice GINI para {selected_country} en el año {selected_year}: {gini}'
    else:
        print(f'Error al obtener los datos para {selected_country}:', resp)


# #Cargo la biblioteca compartida (Programa en lenguaje C)
# lib = ctypes.CDLL('./main.so')

# # Defino el tipo de argumento y el tipo de retorno de la función
# lib.cFloatToInt.argtypes = [ctypes.c_float]
# lib.cFloatToInt.restype = ctypes.c_int
# value_to_convert = lib.cFloatToInt(ctypes.c_float(gini))
# print(f'Valor entero obtenido: {value_to_convert}')