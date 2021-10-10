from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from backoffice.script.get_mailing_list import get_mailing_list
from backoffice.models import Newsletter


@receiver(post_save, sender=Newsletter)
def send_newsletter(sender, instance, created, **kwargs):
    """update this docstring one you figure out where you are going"""
    if created:
        nl_content = instance.format_content()
        context = {
            "nl_title": nl_content['nl_title'],
            "subject_1": nl_content['subject_1'],
            "message_body_1": nl_content['message_body_1'],
            "subject_2": nl_content['subject_2'],
            "message_body_2": nl_content['message_body_2'],
        }
        message_html = render_to_string('backoffice/newsletter_template.html', context)
        mailing_list = get_mailing_list(nl_content['target'].pk)

        email = EmailMessage(
                subject=nl_content['nl_title'],
                body=message_html,
                from_email="latelier-artsetforme@gmail.com",
                bcc=mailing_list,
            )
        email.content_subtype = "html"

        email.send()
