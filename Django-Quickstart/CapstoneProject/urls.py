from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('NuggetServer.urls')),
    path('accounts/', include("django.contrib.auth.urls")),
    path("login/", auth_views.LoginView.as_view(template_name = "login.html"), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
]

=======

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('NuggetServer.urls'))
]
>>>>>>> 7feadbb208b8299c6e9e19bc8ac14d51cd2087b8
