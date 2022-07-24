from django.urls import path 
from . import views
urlpatterns = [
     path('', views.homes, name='homes'),
     path('output', views.output, name="output")
]
