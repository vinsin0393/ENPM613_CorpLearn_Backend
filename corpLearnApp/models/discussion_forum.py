from django.utils import timezone

from django.db import models

class DiscussionForum(models.Model):
    created_date = models.DateTimeField(default=timezone.now)