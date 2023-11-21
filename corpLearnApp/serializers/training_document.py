from rest_framework import serializers

from corpLearnApp.models import TrainingDocument


class TrainingDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingDocument
        fields = '__all__'
