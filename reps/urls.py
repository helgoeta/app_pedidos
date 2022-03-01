from unicodedata import name
from django.urls import path
from reps import views

urlpatterns = [
    path('', views.index, name='index'),
]