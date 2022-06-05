from django.contrib import admin
from .models import Patient, Notification

# Register your models here.
admin.site.register(Patient)
admin.site.register(Notification)

