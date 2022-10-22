from django.urls import path, include
from . import views

app_name = 'NuggetServer'
urlpatterns = [
    path('', views.landing, name='land'),
    path('register/', views.register_request, name="register"),
    path('home/', views.myhomepage, name='homepage'),
    path('flash/', views.flash, name='FlashWifiNugget'),
    path('database/', views.data, name='MACDatabase'),
]