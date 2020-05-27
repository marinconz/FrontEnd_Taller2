from django.shortcuts import render, HttpResponse
import requests

# Create your views here.
def temphum(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' and 'longitud' and 'latitud' and 'tipo_Terreno' in request.GET:
        value = request.GET['value']
        longitud = request.GET['longitud']
        latitud = request.GET['latitud']
        tipo_Terreno = request.GET['tipo_Terreno']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': 'agua', 'value': value, 'longitud':longitud, 'latitud':latitud, 'tipo_Terreno':tipo_Terreno}
            response = requests.post('http://pi1-eafit-marinconz.azurewebsites.net/temphum/', args)
            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://pi1-eafit-marinconz.azurewebsites.net/temphum/')
    # Convierte la respuesta en JSON
    temphum = response.json()
    
    # Rederiza la respuesta en el template measure
    return render(request, "temphum/temphum.html", {'temphums': temphum})
    