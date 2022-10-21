from django.urls import path
from . import views

app_name = 'NuggetServer'
urlpatterns = [
<<<<<<< HEAD
    path('register/', views.register_request, name="register"),
    # path('home/', views.myhomepage, name='homepage'),
    path('flash/', views.mycreate, name='FlashWifiNugget'),
    path('database/', views.mycreate, name='MACDatabase'),
=======
    path('myview/', views.myview, name='myview'),
    path('mycreate/', views.mycreate, name='mycreate')
>>>>>>> 7feadbb208b8299c6e9e19bc8ac14d51cd2087b8
]