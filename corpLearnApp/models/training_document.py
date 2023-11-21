from django.db import models

class TrainingDocument(models.Model):
    document_path = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)