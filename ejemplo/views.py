from django.shortcuts import render
import random

# Create your views here.
def index(request,nombre,apellido,peso,altura):
    años = 47
    pesof = float(peso) #kg
    alturaf = float(altura) #m
    imc = pesof / (alturaf * alturaf)
    #imc=round(peso / (altura * altura))
    return render(request, "ejemplo/saludar.html", {"nombre":nombre, "apellido":apellido, "edad":años, "ind_m_c":imc})

def index2(request):
    return render(request, "ejemplo/saludar.html", {"notas":[1,2,3,4,5,6,7,8,9]})

def index3(request):
  
    a=["Leandro","Sebastian","Marcos"]
    selecto = random.choice(a)
    return render(request, "ejemplo/saludar.html", {"usuario":selecto})