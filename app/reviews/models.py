# app/reviews/models.py

# Django modules
from django.db import models

# Locals
from app.users.models import MyCustomUser
from app.rooms.models import Room

# Create your models here.


# NAMA MODEL/TABEL: Reviews
class Review(models.Model):

	review = models.TextField()
	accuracy = models.IntegerField()
	communication = models.IntegerField()
	cleanliness = models.IntegerField()
	location = models.IntegerField()
	check_in = models.IntegerField()
	value = models.IntegerField()
	user = models.ForeignKey("users.MyCustomUser", on_delete=models.CASCADE)
	room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "Reviews"

	def __str__(self):
		return f"{self.review} - {self.room}"
		# self.room is referring the def __str__(self): return self.name
		# in the Room model
		# The result will look like this: I like this room - Ing Room
