from django.contrib import admin
from .models import *

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'active', 'approved',]

admin.site.register(CustomUser,CustomUserAdmin)



# Register your models here.
