"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ejemplo.views import (index, index2, index3, mostrar_familiares, BuscarFamiliar, 
                            AltaFamiliar, ActualizarFamiliar)
                            #, FamiliarList, FamiliarCrear, 
                            #FamiliarBorrar, FamiliarActualizar)
#from blog.views import index as blog_index
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/<nombre>/<apellido>/<peso>/<altura>/', index), # ESTA ES LA NUEVA FUNCTION
    path('mostrar_notas/', index2), # ESTA ES LA NUEVA FUNCTION
    path('saludar/', index3),
    path('mi-familia/', mostrar_familiares),
    #path('blog/', blog_index), #esto es de la clase pasada
    path('mi-familia/buscar', BuscarFamiliar.as_view()), # NUEVA RUTA PARA BUSCAR FAMILIAR
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('panel-familia/', include('panel_familia.urls')),
    path('travesias/', include('travesias.urls')),
]
