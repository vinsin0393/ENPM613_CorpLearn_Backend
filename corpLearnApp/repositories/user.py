from django.db import IntegrityError, transaction

from corpLearnApp.models import Role


class UserRepository:
    def __init__(self, user_model):
        self.user_model = user_model

    def create_user(self, **data):
        user = self.user_model(**data)
        user.save()
        return user

    def get_user(self, user_id):
        return self.user_model.objects.get(id=user_id)

    def update_user(self, user_id, **data):
        user = self.user_model.objects.get(id=user_id)
        for key, value in data.items():
            setattr(user, key, value)
        user.save()
        return user

    def delete_user(self, user_id):
        self.user_model.objects.filter(id=user_id).delete()

    def get_all_user(self):
        return self.user_model.objects.all()

    def get_or_create_default_user(self, **data):
        default_users = {}
        admin_role = Role.objects.get(id=1)
        user_password = data.get('password')

        with transaction.atomic():
            user_email = 'admin@umd.edu'
            user, created = self.user_model.objects.get_or_create(
                email=user_email,
                defaults={
                    'name': 'Admin',
                    'role': admin_role,
                    'password': user_password
                }
            )
            if user_password:
                user.save()
            default_users[user.email] = user
        return default_users