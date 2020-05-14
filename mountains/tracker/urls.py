from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('mountains/', views.mountains),
    path('hikes/', views.hikes),
]