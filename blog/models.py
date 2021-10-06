from django.db import models
from backoffice.models import Topic


class Blogpost(models.Model):

    category = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=False)
    date_posted = models.TimeField(unique=False)
    content = models.TextField(
        blank=False,
        default="Remplacer ce texte par le contenu"
    )

    def __str__(self):
        return self.title
