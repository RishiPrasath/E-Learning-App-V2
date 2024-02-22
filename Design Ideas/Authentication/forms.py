from django import forms
from .models import *
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'text-input'}))

    class Meta:
        model = PortalUser
        fields = ['username', 'email', 'password', 'user_type', 'photo']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'text-input'}),
            'email': forms.EmailInput(attrs={'class': 'text-input'}),
            'user_type': forms.Select(attrs={'class': 'text-input'}),
            'photo': forms.FileInput(attrs={'class': 'text-input'}),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Perform any additional password validation here if needed
        return password

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.password = make_password(self.cleaned_data['password'])
        if commit:
            instance.save()
        return instance

from django.contrib.auth.hashers import make_password

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        # Hash the entered password for comparison
        hashed_entered_password = make_password(password)

        # Retrieve the user based on the provided email
        try:
            user = PortalUser.objects.get(email=email)
        except PortalUser.DoesNotExist:
            print("Validation Error: User with email does not exist.")
            raise ValidationError('Invalid email or password.')

        # Get the hashed password from the user object
        hashed_user_password = user.password

        # Compare the hashed entered password with the hashed user password
        if hashed_entered_password != hashed_user_password:
            print("Validation Error: Invalid email or password.")
            raise ValidationError('Invalid email or password.')

        # If authentication is successful, the user object will be returned
        print("User authenticated successfully:", user)
        
        return cleaned_data

    
