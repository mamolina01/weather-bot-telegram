import requests,json
from variables import api_key


def getClima(ciudad):
    #Direccion web desde donde solicitaremos la informacion
    base_url="http://api.openweathermap.org/data/2.5/weather?"
    complete_url=base_url+"appid="+api_key+"&q="+str(ciudad)

    #Ejecutamos la consulta
    response=requests.get(complete_url)

    #Obtenemos la respuesta en formato JSON
    x=response.json()

    if x["cod"]==200:
        #En main se encuentra la funcion principal del estado del tiempo
        y=x["main"]
        data=x["weather"]

        #Almacenamos la temperatura
        temperatura=round(y["temp"]-273.15)
        
        #Presion atmosferica
        presionatmosferica=y["pressure"]

        #humedad
        humedad=y["humidity"]
        
        #clima
        clima=data[0]["main"]


        mensaje=f"""
La temperatura de {ciudad} es: {str(temperatura)}° 🌡️
La presion atmosferica de {ciudad} es: {str(presionatmosferica)} 🌎
La humedad de {ciudad} es: {str(humedad)}%💧
El clima de {ciudad} es: {clima} 🌞
        """
        return mensaje