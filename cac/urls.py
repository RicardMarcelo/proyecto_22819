from django.urls import path
from . import views

urlpatterns = [
    path('hola_mundo', views.hola_mundo),
    path('mundial',views.mundial),
    path('saludar',views.saludar,name='saludar_por_defecto'),
    path('saludar/<str:nombre>',views.saludar,name='saludar'),
    path('proyectos/<int:año>/<int:mes>',views.ver_proyectos,name='ver_proyectos'),
]