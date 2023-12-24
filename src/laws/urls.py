from django.urls import path
from . import views

urlpatterns = [
    path('коап/', views.administrative_offences_code, name='administrative_offences_code'),
]
