from rest_framework import serializers

from corpLearnApp.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'role', 'id']
        extra_kwargs = {'password': {'write_only': True}}

