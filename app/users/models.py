# app/users/models.py

# Django modules
from django.contrib.auth.models import AbstractUser
from django.db import models

# Locals

# Create your models here.


# NAMA MODEL/TABEL: MyCustomUser
class MyCustomUser(AbstractUser):

    """ MyCustomUser User Model """

    # Genger choices
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    # Language choices
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"
    LANGUAGE_INDONESIAN = "id"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"), 
        (LANGUAGE_KOREAN, "Korean"), 
        (LANGUAGE_INDONESIAN, "Bahasa")
    )

    # Currency choices
    CURRENCY_USD = "usd"
    CURRENCY_USD = "krw"
    CURRENCY_USD = "rp"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"), 
        (CURRENCY_USD, "KRW"), 
        ( CURRENCY_USD, "RP")
    )

    avatar = models.ImageField(upload_to='uploads/images/users/',blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)  

