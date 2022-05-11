from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(Login)
admin.site.register(hostel)
admin.site.register(food)
admin.site.register(complaint)