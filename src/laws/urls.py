from django.urls import path
from . import views

urlpatterns = [
    path('laws/', views.main, name='main'),
    path('get-administrative-offences-code/', views.get_administrative_offences_code, name='get_administrative_offences_code'),
    path('get-criminal-code/', views.get_criminal_code, name='get_criminal_code'),
]
