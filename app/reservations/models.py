# app/reservations/models.py

# Django modules
from django.db import models

# Locals
from app.users.models import MyCustomUser
from app.rooms.models import Room

# Create your models here.


# NAMA MODEL/TABEL: Reservation
class Reservation(models.Model):

	STATUS_PENDING = "pending"
	STATUS_CONFIRMED = "confirmed"
	STATUS_CANCELED = "canceled"

	STATUS_CHOICES = (
		(STATUS_PENDING, "Pending"),
		(STATUS_CONFIRMED, "Confirmed"),
		(STATUS_CANCELED, "Canceled"),		
	)

	check_in = models.DateField()
	check_out = models.DateField()
	status = models.CharField(
		max_length=12, choices=STATUS_CHOICES,
		default=STATUS_CONFIRMED)
	guest = models.ForeignKey(
		"users.MyCustomUser", on_delete=models.CASCADE)
	room = models.ForeignKey(
		"rooms.Room", on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Reservations"

	def __str__(self):
		return f"{self.room} - {self.check_in} - {self.check_out}"