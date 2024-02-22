from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistrationForm, LoginForm

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print("Email:")  # Debugging print statement to display email
            print(email)
            print("Password:", password)  # Debugging print statement to display password
            user = authenticate(request, username=email, password=password)
            print("User:", user)  # Debugging print statement to display user
            if user is not None:
                print("Login successful.")  # Debugging print statement to indicate successful login
                login(request, user)
                return redirect('home')  # Replace 'home' with the name of your homepage view
            else:
                print("Invalid email or password.")  # Debugging print statement to indicate invalid email or password
                messages.error(request, 'Invalid email or password.')
        else:
            for error in form.non_field_errors():
                messages.error(request, error)
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def registration_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})



def home_page(request):
    return render(request, 'home.html')