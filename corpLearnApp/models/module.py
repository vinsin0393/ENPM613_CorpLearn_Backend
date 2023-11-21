from django.db import models

from corpLearnApp.models.course import Course
from corpLearnApp.models.training_document import TrainingDocument


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()
    training_document = models.ForeignKey(TrainingDocument, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)