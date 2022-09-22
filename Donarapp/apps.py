from django.apps import AppConfig


class DonarappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Donarapp'
    
    def ready(self):
        import Donarapp.signals
