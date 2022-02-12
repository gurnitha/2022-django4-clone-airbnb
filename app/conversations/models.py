# app/conversations/models.py

# Django modules
from django.db import models

# Locals
from app.users.models import MyCustomUser

# Create your models here.


# NAMA MODEL/TABEL: Conversation
class Conversation(models.Model):

	participans = models.ManyToManyField(
		"users.MyCustomUser", blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "Conversations"

	def __str__(self):
		return str(self.created)


# NAMA MODEL/TABEL: Message
class Message(models.Model):

	message = models.TextField()
	user = models.ForeignKey(
		"users.MyCustomUser", on_delete=models.CASCADE)
	conversation = models.ForeignKey(
		"Conversation", on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "Messages"

	def __str__(self):
		return f"{self.user} says: {self.message}"
