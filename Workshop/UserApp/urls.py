from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='C:/Users/brhmi/OneDrive/Bureau/cours_django/Workshop/template/login.html'), name='login'),
]
