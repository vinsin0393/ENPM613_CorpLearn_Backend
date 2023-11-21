from django.db import IntegrityError, transaction

class RoleRepository:
    def __init__(self, role_model):
        self.role_model = role_model


    def create_role(self, **data):
        # Check if a role with the given name already exists to avoid IntegrityError
        role, created = self.role_model.objects.get_or_create(name=data.get('name'), defaults=data)
        return role

    def get_or_create_default_roles(self):
        default_roles = {}
        role_data = [
            {'name': 'Admin', 'description': 'Administrator only'},
            {'name': 'Employee', 'description': 'Employee only'}
        ]

        with transaction.atomic():
            for data in role_data:
                role_name = data['name']
                role, created = self.role_model.objects.get_or_create(name=role_name, defaults=data)
                default_roles[role_name] = role

        return default_roles

    def get_all_role(self):
        return self.model.objects.all()