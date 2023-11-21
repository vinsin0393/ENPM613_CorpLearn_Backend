from rest_framework import serializers

from corpLearnApp.models import DiscussionForumAnswer


class DiscussionForumAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionForumAnswer
        fields = '__all__'