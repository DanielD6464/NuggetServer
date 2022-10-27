from django.urls import path, include
from . import views

app_name = 'NuggetServer'
urlpatterns = [
    path('', views.index, name="index"),
    # path('login/', views.index, name="index"),
    path('register/', views.register_request, name="register"),
    # path('home/', views.homepage, name='homepage'),
    path('flash/', views.flash, name='FlashWifiNugget'),
    path('database/', views.data, name='MACDatabase'),
]