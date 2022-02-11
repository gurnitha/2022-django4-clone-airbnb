# app/reviews/admin.py

# Django modules
from django.contrib import admin

# Locals
from app.reviews.models import Review

# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
	pass


