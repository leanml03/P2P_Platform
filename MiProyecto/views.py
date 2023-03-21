import os
from django.http import HttpResponse
from django.template import Template, Context
#from django.views.decorators.csrf import csrf_exempt
#Aqui se van a crear las vistas //Retornan una respuesta http.

#Request para realizar peticiones

#HTTP Response Para enviar la respuesta usando el protocolo HTTP.

#Esto es una vista
def welcome(request):
	return HttpResponse("<p style='color: red;'>Bienvenido<p>")
def categoriaEdad(request,edad):
	if edad>=18:
		if edad>=60:
			categoria="Tercera Edad"
		else:
			categoria="Adultez"
	else:
		categoria="Infante/Adolescente"
	resultado="<h1>Categoria de la Edad: %s</h1>" %categoria
	return HttpResponse(resultado)

def home(request):
	openTemplate=open(os.path.abspath("MiProyecto/templates/Home.html")) #Se llama a la ruta importando OS para poder correrlo en cualquier computador
	template=Template(openTemplate.read()) #Se lee el HTML y se guarda en template (Se usa Template de libreria de django)
	openTemplate.close() #Se cierra la obtencion del template para no dejarlo vulnerable
	context=Context() #Objeto que nos permite indicar cuales objetos y variables va a utilizar la plantilla
	document=template.render(context) ##Se renderiza el contexto
	return HttpResponse(document) ##Se devuelve el html como respuesta

def register(request):
	openTemplate=open(os.path.abspath("MiProyecto/templates/register.html")) #Se llama a la ruta importando OS para poder correrlo en cualquier computador
	template=Template(openTemplate.read()) #Se lee el HTML y se guarda en template (Se usa Template de libreria de django)
	openTemplate.close() #Se cierra la obtencion del template para no dejarlo vulnerable
	context=Context() #Objeto que nos permite indicar cuales objetos y variables va a utilizar la plantilla
	document=template.render(context) ##Se renderiza el contexto
	return HttpResponse(document) ##Se devuelve el html como respuesta

import json
#@csrf_exempt
def guardar_json(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        with open('data/user', 'w') as f:
            json.dump(data, f)
        return HttpResponse(status=200)	
    else:
        return HttpResponse(status=400)