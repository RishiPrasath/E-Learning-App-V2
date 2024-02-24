from django.http import JsonResponse
from django.views.generic.edit import FormView
from .forms import PortalUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView as AuthLoginView
from django.conf import settings

def registration_page(request):
    if request.method == 'POST':
        form = PortalUserCreationForm(request.POST, request.FILES)
        if form.is_valid(): 
            try:
                form.save()
                return redirect('login')  # Redirect if save is successful
            except Exception as e: 
                return JsonResponse({
                    'success': False, 
                    'message': 'Registration failed. Please contact support.', 
                    'debug_error': str(e) if settings.DEBUG else None 
                })
        else:  # Form is invalid
            return JsonResponse({
                'success': False,  
                'message': 'Form data is invalid.', 
                'errors': form.errors  
            })
    else:  # GET request
        form = PortalUserCreationForm()
        return render(request, 'register.html', {'form': form})

def login_page(request):
    return render(request, 'login.html')










