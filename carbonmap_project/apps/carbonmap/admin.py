from django.contrib import admin
from .models import ReportingEntity, ReportingEntityAddress, UserToEntity

# Register your models here.
admin.site.register(ReportingEntity)
admin.site.register(ReportingEntityAddress)
admin.site.register(UserToEntity)