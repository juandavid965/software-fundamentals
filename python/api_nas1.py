'''
  api: APplication progamming interface
  nasa appi: https://api.nasa.gov/
  developer:juan david 
  script description: get and read data from nasa api comets and others 
  https://api.nasa.gov/neo/rest/v1/neo/3726709?api_key={api_key}
'''
import requests 
import os

os.system("clear")

def get_nasa_data(api_key):
    print("::: COMET INFORMATION :::")
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726709?api_key={api_key}"

    #realizar la solicitud a la API
    response = requests.get(url)
    response.raise_for_status() #=> valida si se presenta algun error en la peticion 
    data = response.json() #convertir la respuesta en porfato JSON (jJS object Notation)

    print(data)

API