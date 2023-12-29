from django.urls import path
from . import views

urlpatterns = [
    path('коап/', views.administrative_offences_code, name='administrative_offences_code'),
    path('ук/', views.criminal_code, name='criminal_code'),
]
