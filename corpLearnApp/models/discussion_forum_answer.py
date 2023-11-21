from django.db import models

from corpLearnApp.models.discussion_forum_question import DiscussionForumQuestion
from corpLearnApp.models.user import User


class DiscussionForumAnswer(models.Model):
    question = models.ForeignKey(DiscussionForumQuestion, related_name='answers', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()