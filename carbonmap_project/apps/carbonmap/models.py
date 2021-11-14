from django.db import models

# Create your models here.

class Reporting_entity(models.Model):
    name = models.CharField(max_length=60)
    id = models.CharField(max_length=60, primary_key=True)
    def __str__(self):
        return self.name