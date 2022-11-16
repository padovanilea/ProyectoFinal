from django.urls import path, include
from travesias.views import CompetidorList, CompetidorCrear, CompetidorActualizar, CompetidorBorrar

urlpatterns = [
    path('', CompetidorList.as_view(), name="competidor-listar"),
    path('crear', CompetidorCrear.as_view(), name="competidor-crear"),
    path('<int:pk>/actualizar', CompetidorActualizar.as_view(), name="competidor-actualizar"),
    path('<int:pk>/borrar', CompetidorBorrar.as_view(), name="competidor-borrar"),
]