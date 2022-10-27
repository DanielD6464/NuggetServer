from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('', include('NuggetServer.urls')),
    path('accounts/', include("django.contrib.auth.urls")),
]

