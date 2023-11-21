from rest_framework import serializers

from corpLearnApp.models import  EmployeeConcern


class EmployeeConcernSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeConcern
        fields = '__all__'