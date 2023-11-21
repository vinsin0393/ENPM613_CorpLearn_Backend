from django.db import IntegrityError, transaction
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
        user = {'name': 'Admin', 'email': 'admin@umd.edu', 'role_id': 1, 'password': data['password']}
        with transaction.atomic():
            user_email = user['email']
            email, created = self.user_model.objects.get_or_create(email = user_email, defaults=data)
            default_users[email] = email


        return default_users