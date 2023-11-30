from django.db import models
from django.utils import timezone

from corpLearnApp.models import User, Course


class EmployeeCourse(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    deadline = models.DateField(default=timezone.now)
    status = models.CharField(max_length=50)
    data = models.TextField(blank=True, null=True)