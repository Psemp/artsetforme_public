from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=200, unique=True, default="General")

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    global_title = models.CharField(max_length=255, unique=False, default="Newsletter", blank=False)
    subject_1 = models.CharField(max_length=255, unique=False, default="Titre section 1", blank=False)
    target = models.ForeignKey(Topic, on_delete=models.CASCADE)
    body_1 = models.TextField(unique=False, blank=False)
    image_body_1 = models.ImageField(upload_to="newsletter_files/", blank=True)
    subject_2 = models.CharField(max_length=255, unique=False, blank=True)
    body_2 = models.TextField(unique=False, blank=True)
    image_body_2 = models.ImageField(upload_to="newsletter_files/", blank=True)
    attachment = models.FileField(upload_to="newsletter_files/", blank=True)
    time_submitted = models.DateTimeField(auto_created=True)

    def format_content(self):
        if self.subject_2 is None and self.body_2 is None:
            content = {
                "nl_title": self.global_title,
                "target": self.target,
                "subject_1": self.subject_1,
                "message_body_1": " ".join(self.body_1.split("\r\n")),
                "attachments": []
            }
            if self.image_body_1 is not None:
                content["image_1_src"] = self.image_body_1,
            if self.attachment is not None:
                content["attachments"].append(self.attachment_1)

        elif self.subject_2 is not None and self.body_2 is not None:
            content = {
                "nl_title": self.global_title,
                "target": self.target,
                "subject_1": self.subject_1,
                "message_body_1": " ".join(self.body_1.split("\r\n")),
                "subject_2": self.subject_2,
                "message_body_2": " ".join(self.body_2.split("\r\n")),
                "attachments": []
            }
            if self.image_body_1 is not None:
                content["image_1_src"] = self.image_body_1,
            if self.image_body_2 is not None:
                content["image_2_src"] = self.image_body_2,
            if self.attachment is not None:
                content["attachments"].append(self.attachment)

        return content

    def __str__(self):
        return self.global_title
