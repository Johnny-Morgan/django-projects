from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('mountains/', views.mountains, name="mountains"),
    path('hikes/', views.hikes, name="hikes"),
    path('peak/<str:pk>/', views.peak, name="peak"),
    path('add_mountain_form/', views.addMountain, name="add_mountain"),
    path('update_mountain/<str:pk>/', views.updateMountain, name="update_mountain"),
    path('delete_mountain/<str:pk>/', views.deleteMountain, name="delete_mountain"),
    path('hike/<str:pk>/', views.hike, name="hike"),
]