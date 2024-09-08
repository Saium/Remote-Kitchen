from django.contrib import admin

# Register your models here.

from .models import CustomUser

admin.site.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_owner', 'is_employee']