from django.contrib import admin

# Register your models here.

from .models import Session, CustomUser

admin.site.register(Session)
admin.site.register(CustomUser)
