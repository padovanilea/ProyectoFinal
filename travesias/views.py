from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from ejemplo.models import Competidor

# Create your views here.
class CompetidorList(ListView):
    model = Competidor

class CompetidorCrear(CreateView):
    model = Competidor
    success_url = "/travesias"
    fields = ["apellido", "nombre", "dni", "prueba", "emerg_contacto", "emerg_llamar"]

class CompetidorActualizar(UpdateView):
    model = Competidor
    success_url = "/travesias"
    fields = ["apellido", "nombre", "dni", "prueba", "emerg_contacto", "emerg_llamar"]

class CompetidorBorrar(DeleteView):
    model = Competidor
    success_url = "/travesias"