from django.urls import path
from .views import *

urlpatterns = [
    path('register/', registration_page, name='register'),
    #Redirect to login.html in templates folder

    path('login/', login_page, name='login'),
]
