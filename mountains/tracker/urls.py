from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('mountains/', views.mountains, name="mountains"),
    path('hikes/', views.hikes, name="hikes"),
    path('peak/<str:pk>/', views.peak, name="peak"),
]