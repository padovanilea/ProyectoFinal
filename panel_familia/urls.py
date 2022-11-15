from django.urls import path, include
from panel_familia.views import FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar

urlpatterns = [
    path('', FamiliarList.as_view(), name="familiar-listar"),
    path('crear', FamiliarCrear.as_view(), name="familiar-crear"),
    path('<int:pk>/borrar', FamiliarBorrar.as_view(), name="familiar-borrar"),
    path('<int:pk>/actualizar', FamiliarActualizar.as_view(), name="familiar-actualizar"),
]