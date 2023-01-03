from django.urls import path 
from . import views

urlpatterns = [
    path('jsonGetAllUser/',views.jsonGetAllUser, name="userData"),
    path('tempGetAllUser/',views.TempGetAllUser, name="userData"),
]
