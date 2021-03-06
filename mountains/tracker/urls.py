from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
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
    path('add_hike_form/', views.addHike, name="add_hike"),
    path('update_hike/<str:pk>/', views.updateHike, name="update_hike"),
    path('delete_hike/<str:pk>/', views.deleteHike, name="delete_hike"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/', views.userPage, name="user-page"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)