from django.apps import AppConfig


class CorplearnappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'corpLearnApp'

    def ready(self):
        from .services import UserService
        UserService.add_default_role()
        UserService.add_test_admin_user()