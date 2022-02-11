# app/rooms/admin.py

# Django modules
from django.contrib import admin

# Locals
from app.rooms.models import (
	RoomType, Amenity,
	Facility, HouseRule, 
	Room, Photo)

# Register your models here.


admin.site.register(RoomType)
admin.site.register(Amenity)
admin.site.register(Facility)
admin.site.register(HouseRule)
admin.site.register(Room)
admin.site.register(Photo)
