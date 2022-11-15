from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from ejemplo.models import Familiar

# Create your views here.
class FamiliarList(ListView):
    model = Familiar

class FamiliarCrear(CreateView): # FamiliarCrear hereda de CreateView que ya sabe como trabajar con post o get
    model = Familiar
    success_url = "/panel-familia" # Especifica a que lugar se va luego de crear
    fields = ["nombre", "direccion", "numero_pasaporte"]

class FamiliarBorrar(DeleteView):
    model = Familiar
    success_url = "/panel-familia"

class FamiliarActualizar(UpdateView):
    model = Familiar
    success_url = "/panel-familia"
    fields = ["nombre", "direccion", "numero_pasaporte"]
