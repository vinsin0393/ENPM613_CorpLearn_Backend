from rest_framework import serializers

from corpLearnApp.models import DiscussionForumQuestion


class DiscussionForumQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionForumQuestion
        fields = '__all__'