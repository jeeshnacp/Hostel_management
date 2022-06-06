from django.contrib import admin

# Register your models here.
from app import models

admin.site.register(models.Login)
admin.site.register(models.hostel)
admin.site.register(models.food)
admin.site.register(models.complaint)
admin.site.register(models.Student)
admin.site.register(models.parent)
admin.site.register(models.staff)
admin.site.register(models.fees)
admin.site.register(models.payment)
admin.site.register(models.Notification)