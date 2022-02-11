# app/rooms/models.py

# Django modules
from django.db import models
from django_countries.fields import CountryField

# Locals
# from django.contrib.auth.models import AbstractUser

# Create your models here.


# NAMA MODEL/TABEL: RoomType
class RoomType(models.Model):

	name = models.CharField(max_length=80)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


	class Meta:
		verbose_name = "Room Type"

	def __str__(self):
		return self.name


# NAMA MODEL/TABEL: Amenity
class Amenity(models.Model):

	name = models.CharField(max_length=80)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


	class Meta:
		verbose_name = "Amenities"

	def __str__(self):
		return self.name


# NAMA MODEL/TABEL: Facility
class Facility(models.Model):

	name = models.CharField(max_length=80)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


	class Meta:
		verbose_name = "Facilities"

	def __str__(self):
		return self.name


# NAMA MODEL/TABEL: HouseRule
class HouseRule(models.Model):

	name = models.CharField(max_length=80)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


	class Meta:
		verbose_name = "House Rule"

	def __str__(self):
		return self.name


# NAMA MODEL/TABEL: Room
class Room(models.Model):

	name = models.CharField(max_length=140)
	description = models.TextField()
	country = CountryField()
	city = models.CharField(max_length=80)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	address = models.CharField(max_length=140)
	guests = models.IntegerField()
	beds = models.IntegerField()
	bedrooms = models.IntegerField()
	baths = models.IntegerField()
	check_in = models.TimeField()
	check_out = models.TimeField()
	instant_book = models.BooleanField(default=False)
	# host = models.ForeignKey(MyCustomUser, on_delete=models.CASCADE)
	room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
	amenities = models.ManyToManyField(Amenity, blank=True)
	facilities = models.ManyToManyField(Facility, blank=True)
	house_rules = models.ManyToManyField(HouseRule, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Rooms"

	def __str__(self):
		return self.name


# NAMA MODEL/TABEL: Photo
class Photo(models.Model):

	caption = models.CharField(max_length=80)
	file = models.ImageField(upload_to='uploads/images/photos/')
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Photos"

	def __str__(self):
		return self.caption