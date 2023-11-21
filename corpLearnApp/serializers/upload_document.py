from rest_framework import serializers

class UploadDocumentSerializer(serializers.Serializer):
    file = serializers.FileField()
    course_id = serializers.IntegerField()
    content = serializers.CharField()
