from django.utils import timezone

from django.db import models
from corpLearnApp.models.course import Course

class DiscussionForum(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)