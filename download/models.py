from django.db import models


class Downloadable(models.Model):
    name = models.CharField(max_length=255, blank=False)
    short_description = models.CharField(max_length=455, blank=True)
    file = models.FileField(blank=False, upload_to="documents")
    date_uploaded = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name
