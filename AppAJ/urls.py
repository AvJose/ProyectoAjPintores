from django.urls import path
from AppAJ.models import Trabajos_realizados
from AppAJ import views

urlpatterns = [
    path('', views.inicio, name= "inicio"),
    path('trabajos_realizados/', views.trabajos_realizados, name="trabajos_realizados"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('materiales/', views.materiales, name="materiales"),
    path('contacto/', views.contacto, name="contacto"),
    


    
    

]

