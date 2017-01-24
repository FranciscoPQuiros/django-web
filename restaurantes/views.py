from pymongo import MongoClient
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.db import models
from django.conf import settings

# Create your models here.
client = settings.CLIENT
db = client.test

@login_required
def index(request):
	texto = ""
	restaurant = db.restaurant.find()[0:1]
	for rest in restaurant:
		texto += rest.get("name") + " | ";
		texto +=  rest.get("borough") + " | ";
		texto +=  rest.get("cuisine") + ";";
	return HttpResponse(texto)

def test(request):
    return render(request,'test.html', {})

@login_required
def registro(request):
	if request.method == 'GET':
		return render(request,'registro.html', {})
	if request.method == 'POST':
		nombre = request.POST.get('name')
		ciudad = request.POST.get('borough')
		cocina = request.POST.get('cuisine')
		db.restaurantes.insert({"borough":ciudad,"cuisine":cocina,"name":nombre})
		return HttpResponse('Method POST!' + str(nombre) + str(ciudad))
	
