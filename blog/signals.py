from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from .models import Blogpost
from backoffice.script.get_mailing_list import get_mailing_list


@receiver(post_save, sender=Blogpost)
def send_notification(sender, instance, created, **kwargs):
    """This signal detects if a new post is created, fetches the
    relevant mailing list and sends mass mail to subscribed users"""
    if created:
        mailing_list = []
        topic_id = instance.category_id
        mailing_list = get_mailing_list(topic_id)
        context = {
            "title": instance.title,
            "category": instance.category,
        }
        message_html = render_to_string('backoffice/newsletter_template.html', context)
        notification = EmailMessage(
            subject=f"Nouveau post dans la catégorie{instance.category}",
            from_email="latelier-artsetforme@gmail.com",
            bcc=mailing_list,
            body=message_html,
        )
        notification.content_subtype = "html"
        notification.send()
