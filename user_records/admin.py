from django.contrib import admin
from django.db import models
from djongo import models as djongo_models
from .models import User, Product

# PostgreSQL Model Admin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

# MongoDB Model Admin (using DjongoAdmin)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity')
