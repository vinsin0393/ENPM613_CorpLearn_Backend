from rest_framework import serializers

from corpLearnApp.models import EmployeeCourse


class EmployeeCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCourse
        fields = '__all__'
