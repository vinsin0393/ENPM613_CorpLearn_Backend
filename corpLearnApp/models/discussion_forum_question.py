from django.db import models

from corpLearnApp.models.discussion_forum import DiscussionForum
from corpLearnApp.models.user import User


class DiscussionForumQuestion(models.Model):
    discussion_forum = models.ForeignKey(DiscussionForum, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()