from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import PortalUser
from django.core.exceptions import ValidationError
from .validators import *
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

class PortalUserCreationForm(UserCreationForm):

    username = forms.CharField(
        required=True, # This field is required
        label=_("Username"),# 
        validators=[validate_unique_username] # This field should be unique
    )
    email = forms.EmailField(
        required=True, # This field is required
        label=_("Email"), # This is the label for the field
        validators=[validate_email_format, validate_unique_email] # This field should be unique
    )
    user_type = forms.ChoiceField(
        choices=PortalUser.USER_TYPE_CHOICES, # This is the list of choices
        required=True, # This field is required
        label=_("User Type"), # This is the label for the field
        validators=[validate_user_type] # This field should be unique
    )
    photo = forms.ImageField(
        required=False,  # This field is not required
        label=_("Photo"), # This is the label for the field
        validators=[validate_image] # This field should be unique
    )

    class Meta(UserCreationForm.Meta):
        model = PortalUser
        fields = UserCreationForm.Meta.fields + ('email', 'user_type', 'photo',) # Include the 'email' and 'user_type' fields

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        errors = []
        
        # Validate the password
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

        # Validate the password
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

        
    # Save the user
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.user_type = self.cleaned_data["user_type"]
        if self.cleaned_data["photo"]:
            user.photo = self.cleaned_data["photo"]
        if commit:
            user.save()
        return user




class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")  # Change the label of the 'username' field
    password = forms.CharField(label="Password", widget=forms.PasswordInput)  # Change the label of the 'password' field

    '''
    Check if user exists in the PortalUser model

    If not, Raise a validation error
    '''
    def clean_username(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        print("Username: ", username)
        print("Password: ", password)
        if not PortalUser.objects.filter(username=username).exists():
            print("User does not exist")
            raise ValidationError(_("A user with that username does not exist."))
        return username
    




class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = StatusUpdate
        fields = ['content'] # Only include the desired fields




class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'subject'] # Only include the desired fields

    def clean(self):
        cleaned_data = super().clean()  # This performs Django's default validation
        for field_name in self.fields:
            if not cleaned_data.get(field_name):  
                raise forms.ValidationError(f"{field_name} is required.")
        return cleaned_data






class TopicCreationForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name', 'description']  # Only include the desired fields

    def clean(self):
        cleaned_data = super().clean()

        # You can keep your validation logic as is
        for field_name in self.fields:
            if not cleaned_data.get(field_name):
                raise forms.ValidationError(f"{field_name} is required.")

        return cleaned_data
    



class CourseMaterialUploadForm(forms.ModelForm):
    class Meta:
        model = CourseMaterial
        fields = ('title', 'file') # Only include the desired fields




class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['user', 'content']  # Include 'user' and 'content' fields

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Pop the 'user' argument from kwargs
        super(ChatMessageForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['user'].initial = user  # Set the initial value for the 'user' field
            self.fields['user'].widget = forms.HiddenInput()  # Hide the 'user' field in the form




class ChatGroupForm(forms.ModelForm):
    class Meta:
        model = ChatGroup # Use the ChatGroup model
        fields = ['name', 'course', 'topic'] # Include 'name', 'course', and 'topic' fields