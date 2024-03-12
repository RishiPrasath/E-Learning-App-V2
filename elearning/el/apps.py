from django.apps import AppConfig


class ElConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'el'

    def ready(self):
        print("elearning app is ready")
        
