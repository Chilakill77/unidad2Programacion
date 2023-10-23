#Cabrera Luna Kevin
import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Dolores Hidalgo"
dest = "San Miguel de Allende"
key = "kJI2zNJ9v75CAlaxsEnXHkyutNojJ0tN"
#Extrae la ruta y la ID de sesion
url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
json_data = requests.get(url).json()
print (json_data ['route'] ['sessionId'])
#Extrae la distancia y el tiempo
distance= (json_data ['route']['distance'])
time = (json_data['route']['time'])
print (distance)
print (time)
#Extrae el primer elemento legs
formattedTime= (json_data ['route']['legs']['formattedTime'])
print (formattedTime)
#Paso DOS
#print("URL: " + (url))

#json_data = requests.get(url).json()
#json_status = json_data["info"]["statuscode"]

#if json_status == 0:
#    print("API Status: " + str(json_status) + " = A successful route call.\n")
