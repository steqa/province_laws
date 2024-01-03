from django.urls import path
from . import views

urlpatterns = [
    path('laws/', views.main, name='main'),
]
