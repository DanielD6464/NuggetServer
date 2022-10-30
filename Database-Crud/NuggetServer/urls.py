from django.urls import path, include
from . import views

app_name = 'NuggetServer'
urlpatterns = [
    path('register/', views.register_request, name="register"),
    path('home/', views.index, name='homepage'),
    path('flash/', views.flash, name='FlashWifiNugget'),
    path('database/', views.mac_database, name='MACDatabase'),
]