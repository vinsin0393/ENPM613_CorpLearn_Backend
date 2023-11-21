from django.db import models

from corpLearnApp.models.user import User


class EmployeeConcern(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now=True)
    content = models.TextField()