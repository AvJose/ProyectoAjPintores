from django.urls import path
from AppAJ.models import Trabajos_realizados
from AppAJ import views

urlpatterns = [
    path('', views.inicio, name= "inicio"),
    path('paginas/', views.materiales, name="paginas"),
    path('nosotros.html/', views.nosotros, name="nosotros"),
    path('materiales/', views.materiales, name="materiales"),
    path('contacto.html/', views.contacto, name="contacto"),
    path('trabajos_realizados.html/', views.trabajos_realizados, name="trabajos_realizados"),
    path('acerca_de_mi.html/', views.acerca_de_mi, name="acerca_de_mi"),
    
    
    


    
    

]

