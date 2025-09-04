# Discontinued feature, passing to minimize impact
#  @receiver(post_save, sender=Blogpost)
def send_notification(sender, instance, created, **kwargs):
    pass
    # """This signal detects if a new post is created, fetches the
    # relevant mailing list and sends mass mail to subscribed users"""
    # if created:
    #     mailing_list = []
    #     topic_id = instance.category_id
    #     mailing_list = get_mailing_list(topic_id)
    #     context = {
    #         "title": instance.title,
    #         "category": instance.category,
    #     }
    #     message_html = render_to_string('blog/notification_template.html', context)
    #     notification = EmailMessage(
    #         subject=f"Nouveau post dans la catégorie{instance.category}",
    #         from_email="latelier-artsetforme@gmail.com",
    #         bcc=mailing_list,
    #         body=message_html,
    #     )
    #     notification.content_subtype = "html"
    #     notification.send(fail_silently=True)
