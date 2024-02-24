from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    # ... other URL patterns ... 
    path('', auth_views.LoginView.as_view(), name='login'),  # Redirect root URL to login
    path('home/', home_page, name='home'),
    path('register/', registration_page, name='register'),
    path('logout/', auth_views.LoginView.as_view(), name='logout'), 
]