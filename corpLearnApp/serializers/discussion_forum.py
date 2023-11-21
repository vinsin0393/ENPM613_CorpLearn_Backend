from rest_framework import serializers

from corpLearnApp.models import DiscussionForum


class DiscussionForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionForum
        fields = '__all__'