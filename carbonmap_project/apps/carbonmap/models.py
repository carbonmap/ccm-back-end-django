from django.db import models

# Create your models here.

class ReportingEntity(models.Model):
    name = models.CharField(max_length=255)
    id = models.CharField(max_length=255, primary_key=True)
    def __unicode__(self):
        return self.name

class ReportingEntityAddress(models.Model):
    id = models.CharField(max_length=60, primary_key=True)
    street_address = models.CharField(max_length=255)
    address_locality = models.CharField(max_length=255)
    address_region = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=15)
    address_country = models.CharField(max_length=2)
    def __unicode__(self):
        return self.street_address 

class UserToEntity(models.Model):
    user_id = models.CharField(max_length=255)
    entity_id = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
