# app/reservations/admin.py

# Django modules
from django.contrib import admin

# Locals
from app.reservations.models import Reservation

# Register your models here.

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
	pass

