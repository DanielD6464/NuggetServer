from django.urls import path
from . import views
from .views import myregister

app_name = 'NuggetServer'
urlpatterns = [
    path('register/', myregister, name="registeruser"),
    # path('home/', views.myhomepage, name='homepage'),
    path('flash/', views.mycreate, name='FlashWifiNugget'),
    path('database/', views.mycreate, name='MACDatabase'),
]