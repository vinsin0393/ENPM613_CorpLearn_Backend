from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    def allow_edit(self):
        return self.name in ['Admin']