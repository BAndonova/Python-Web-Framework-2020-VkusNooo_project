
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class UserProfile(models.Model):
    date_of_birth = models.DateTimeField(null=True, blank=True)
    creation_date = models.DateTimeField(default=now, editable=False)
    profile_image = models.ImageField(
        upload_to="profiles/", blank=True,
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

