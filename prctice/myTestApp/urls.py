from django.urls import path 
from . import views

urlpatterns = [
    path('getTestUser/',views.getTestUser ,  name="userData"),
    path('PostTestUser/',views.PostTestUser ,  name="userData"),
]