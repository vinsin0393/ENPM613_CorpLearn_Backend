from django.db import models

from corpLearnApp.models.user import User


class Course(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    time_to_complete = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)