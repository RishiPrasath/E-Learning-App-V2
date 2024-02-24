from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class PortalUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    user_type = models.CharField(max_length=7, choices=USER_TYPE_CHOICES, default='student')
    email = models.EmailField(_('email address'), unique=True)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    real_name = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(blank=True)
    qualifications = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Portal User'
        verbose_name_plural = 'Portal Users'
        # Specify related_name for groups and user_permissions to resolve conflict
        permissions = [
            # Define any custom permissions for your PortalUser here
        ]

    def __str__(self):
        return self.username
