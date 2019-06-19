from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import datetime


# To faciliate Django to work with our custom user model
class user_profile_manager(BaseUserManager):
    def create_user(self, username, name, password, date_of_birth):
        # Create new user profile object
        if not username:
            raise ValueError("User must have an Username")
        user = self.model(username=username, name=name,
                          date_of_birth=date_of_birth)
        #   hasing the password and saving it to the same database
        user.set_password(password)
        user.save(self.db)
        return user


# Represents the User model of the API
class user_profile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=datetime.date.today)
    is_active = models.BooleanField(default=True)
    objects = user_profile_manager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
