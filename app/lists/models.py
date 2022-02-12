# app/lists/models.py

# Django modules
from django.db import models

# Locals
from app.users.models import MyCustomUser
from app.rooms.models import Room

# Create your models here.


# NAMA MODEL/TABEL: List
class List(models.Model):

	name = models.CharField(max_length=80)
	user = models.ForeignKey("users.MyCustomUser", on_delete=models.CASCADE)
	room = models.ManyToManyField("rooms.Room", blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "Lists"

	def __str__(self):
		return self.name