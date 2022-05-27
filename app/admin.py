from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(Login)
admin.site.register(hostel)
admin.site.register(food)
admin.site.register(complaint)
admin.site.register(student)
admin.site.register(parent)
admin.site.register(staff)
admin.site.register(fees)
admin.site.register(payment)
admin.site.register(Notification)