# app/lists/admin.py

# Django modules
from django.contrib import admin

# Locals
from app.lists.models import List

# Register your models here.

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
	pass