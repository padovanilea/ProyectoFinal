from django.shortcuts import render
import random
from ejemplo.models import Familiar
from ejemplo.forms import Buscar # <--- NUEVO IMPORT
from django.views import View # <-- NUEVO IMPORT 

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

def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        #se chequea que no haya mas de 100 caracteres
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})

        return render(request, self.template_name, {"form": form})