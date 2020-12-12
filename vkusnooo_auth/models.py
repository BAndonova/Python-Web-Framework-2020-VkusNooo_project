
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

from cloudinary import models as cloudinary_models

class UserProfile(models.Model):
    date_of_birth = models.DateTimeField(null=True, blank=True)
    creation_date = models.DateTimeField(default=now, editable=False)
    profile_image = cloudinary_models.CloudinaryField('image', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.id}; {self.user.username}; {self.creation_date}; {self.date_of_birth}'

    # def count_profiles(self, profile):
    #     profiles_count = UserProfile.user.count()


