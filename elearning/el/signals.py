from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
from django.conf import settings
from .models import CourseMaterial

@receiver(post_delete, sender=CourseMaterial)
def delete_file_on_delete(sender, instance, **kwargs):

    print('Signal received')

    print(instance.file.path)

    if instance.file: 
        if os.path.isfile(instance.file.path):
            status = os.remove(instance.file.path)
            # Print status of file removal
            print('Delete file status:',status)
    else:
        print('File not found')