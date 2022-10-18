from django.shortcuts import render

# Create your views here.
def index(request,nombre,apellido):
    años = 47
    peso = 77 #kg
    altura = 1.77 #m
    imc = int(peso / (altura * altura))
    #imc=round(peso / (altura * altura))
    return render(request, "ejemplo/saludar.html", {"nombre":nombre, "apellido":apellido, "edad":años, "ind_m_c":imc})

def index2(request):
    return render(request, "ejemplo/saludar.html", {"notas":[1,2,3,4,5,6,7,8,9]})

    