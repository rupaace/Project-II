from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'))


class User(AbstractUser):
    username = None
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    })
    gender = models.CharField(max_length=10, blank=True, null=True, default="")
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    image = models.ImageField( upload_to='Profile', height_field=224, width_field=225, max_length=None,default="", null=True, blank=True)
    education = models.CharField(max_length=500, default="", null=True, blank=True)
    skills = models.CharField(max_length=500, default="", null=True, blank=True)
    former_job = models.CharField(max_length=500, default="", null=True, blank=True)
    eligibility = models.CharField(max_length=500, default="", null=True, blank=True)
    experience = models.CharField(max_length=500, default="", null=True, blank=True)
    website = models.CharField(max_length=500, default="", null=True, blank=True)
    phone_number = models.CharField(max_length=500, default="", null=True, blank=True)
    bio = models.TextField(default="")


    def __unicode__(self):
        return self.email

    objects = UserManager()
