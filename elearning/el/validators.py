from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import check_password 
import re 
import datetime
from .models import *
# 1. Email Validator

# User Type Validator
def validate_unique_email(email):
    from django.contrib.auth.models import User  # Import the User model
    if PortalUser.objects.filter(email=email).exists():
        raise ValidationError(_("A user with that email already exists."))

# Email Format Validator
def validate_email_format(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(regex, email):
        raise ValidationError(_("Enter a valid email address."))  
    

# 1.5. Username Unique Validator
def validate_unique_username(username):
    if PortalUser.objects.filter(username=username).exists():
        raise ValidationError(_("A user with that username already exists."))


# 2. User Type Validator
    
# User Type Validator    
def validate_user_type(user_type):
    from .models import PortalUser  
    if user_type not in [choice[0] for choice in PortalUser.USER_TYPE_CHOICES]:
        raise ValidationError(_("Select a valid choice. {} is not one of the available choices.").format(user_type))
 


# 3. Password Complexity Validators
    
# Password Length Validator    
def validate_password_length(password):
    errors = []  # Collect errors
    min_length = 8
    if len(password) < min_length:
        errors.append(f"Password must be at least {min_length} characters long.")
    return errors  # Return collected errors (might be empty)

def validate_password_has_lowercase(password):
    errors = []
    if not re.search('[a-z]', password):
        errors.append("Password must contain at least one lowercase letter.")
    return errors

def validate_password_has_uppercase(password):
    errors = []
    if not re.search('[A-Z]', password):
        errors.append("Password must contain at least one uppercase letter.")
    return errors

def validate_password_has_number(password):
    errors = []
    if not re.search('[0-9]', password):
        errors.append("Password must contain at least one number.")
    return errors

def validate_password_has_special_character(password):
    errors = []
    regex = re.compile('[@_!#$%^^&*()<>?/\|}{~:]')
    if not regex.search(password):
        errors.append("Password must contain at least one special character.")
    return errors



# 4. Image Validator
    
'''
Valid Image file formats: JPEG, PNG , GIF , BMP , TIFF , SVG

Validate Image size: 2MB

'''

def validate_image(image):

    file_size = image.size
    limit_mb = 2
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError(_("File size exceeds 2MB limit."))
    if not image.name.endswith(('.jpg', '.png', '.gif', '.bmp', '.tiff', '.svg')):
        raise ValidationError(_("Invalid file format. Supported formats are JPEG, PNG, GIF, BMP, TIFF, SVG."))

