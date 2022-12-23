from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index' ),
    path('minhaConsulta/', views.revisaoConsulta, name="minha_consulta")
]