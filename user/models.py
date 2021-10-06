from django.db import models
from django.contrib.auth.models import User
from backoffice.models import Topic


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.ManyToManyField(Topic, related_name="subscriptions", blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
