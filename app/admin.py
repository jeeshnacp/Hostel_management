from django.contrib import admin

# Register your models here.
from app import models

admin.site.register(models.Login)
admin.site.register(models.Hostel)
admin.site.register(models.Food)
admin.site.register(models.Complaint)
admin.site.register(models.Student)
admin.site.register(models.Parent)
admin.site.register(models.Staff)
admin.site.register(models.Fees)
admin.site.register(models.Payment)
admin.site.register(models.Notification)
admin.site.register(models.BookRoom)
