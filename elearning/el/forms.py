from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import PortalUser
from django.core.exceptions import ValidationError
from .validators import *
class PortalUserCreationForm(UserCreationForm):

    username = forms.CharField(
        required=True,
        label=_("Username"),
        validators=[validate_unique_username]
    )



    email = forms.EmailField(
        required=True, 
        label=_("Email"),
        validators=[validate_email_format, validate_unique_email]
    )
    user_type = forms.ChoiceField(
        choices=PortalUser.USER_TYPE_CHOICES, 
        required=True, 
        label=_("User Type"),
        validators=[validate_user_type] 
    )
    photo = forms.ImageField(
        required=False, 
        label=_("Photo"),
        validators=[validate_image]
    )

    class Meta(UserCreationForm.Meta):
        model = PortalUser
        fields = UserCreationForm.Meta.fields + ('email', 'user_type', 'photo',)

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        errors = []

        errors += validate_password_length(password1)
        errors += validate_password_has_lowercase(password1)
        errors += validate_password_has_uppercase(password1)
        errors += validate_password_has_number(password1)
        errors += validate_password_has_special_character(password1)

        if errors:
            # Combine specific errors with the list of requirements
            message = "Your password doesn't meet the requirements: " + ', '.join(errors)
            raise ValidationError(message)  

        return password1
    
    def clean_password2(self):
        cleaned_data = super().clean()
        password2 = cleaned_data.get('password2')
        errors= []


        errors+=validate_password_length(password2)
        errors+=validate_password_has_lowercase(password2)
        errors+=validate_password_has_uppercase(password2)
        errors+=validate_password_has_number(password2)
        errors+=validate_password_has_special_character(password2)

        if errors:
            # Combine specific errors with the list of requirements
            message = "Your password doesn't meet the requirements: " + ', '.join(errors)
            raise ValidationError(message)
        return password2

        

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.user_type = self.cleaned_data["user_type"]
        if self.cleaned_data["photo"]:
            user.photo = self.cleaned_data["photo"]
        if commit:
            user.save()
        return user
