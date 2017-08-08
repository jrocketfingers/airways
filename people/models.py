from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)


class Guest(UserProfile):
    pass


class GenericEmployee(UserProfile):
    pass


class Employee(GenericEmployee):
    pass


class Pilot(GenericEmployee):
    pass


class Stewardess(GenericEmployee):
    pass
