from django.contrib import admin
from .models import User

@admin.register(User)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'subscription_plan')
