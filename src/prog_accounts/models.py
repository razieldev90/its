from django.db import models
from django.contrib.auth.models import AbstractUser

# from profiles.models import Profile


class User(AbstractUser):

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        # profile = Profile.objects.create(user=self)
        # if not profile:
        #     print("NO PROFILE CREATED")
        print("USER CREATED SCCESSFULLY")
        return super().save()
