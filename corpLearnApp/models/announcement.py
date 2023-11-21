from django.db import models

from corpLearnApp.models.user import User


class Announcement(models.Model):
    announcement_date = models.DateTimeField(auto_now=True)
    content  = models.TextField(blank=True, null=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)