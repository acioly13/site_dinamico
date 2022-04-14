from django.contrib.auth import views as auth_views, views
from django.contrib.auth.views import LoginView
from django.urls import path, include
from simplemooc.accounts.views import register, dashboard, edit, edit_password
import simplemooc.core.templates
from . import views
import simplemooc.settings

app_name = 'accounts'
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', LoginView.as_view(template_name='accounts/logar.html'), name='login'),
    path('sair/', auth_views.LogoutView.as_view(template_name='home.html'), name="logout"),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('edit_password/', edit_password, name='edit_password')



]
