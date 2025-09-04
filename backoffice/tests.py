from django.test import TestCase
from .models import Newsletter, Topic
from .script import get_mailing_list
from user.models import Profile
from django.contrib.auth.models import User
import datetime

# Create your tests here.


class NewsletterTest(TestCase):

    def setUp(self):
        Topic.objects.create(name="Test category")
        nl_target = Topic.objects.get(name="Test category")
        Newsletter.objects.create(
            global_title="Newletter Test",
            subject_1="Fire and Ice",
            target=nl_target,
            body_1='Some say the world will end in Fire, Some say in Ice',
            time_submitted=datetime.datetime.now()
            )
        self.nl_test = Newsletter.objects.get(global_title="Newletter Test")

    def test_nl_save(self):
        nl = Newsletter.objects.last()
        self.assertEqual(nl.global_title, self.nl_test.global_title)
        self.assertEqual(nl.subject_1, self.nl_test.subject_1)
        self.assertEqual(nl.target, self.nl_test.target)
        self.assertEqual(nl.body_1, self.nl_test.body_1)

    def signal_received(self):
        pass


class MailinglistTest(TestCase):

    def setUp(self):
        Topic.objects.create(name="Test topic for mail")
        self.topic = Topic.objects.get(name="Test topic for mail")
        self.credentials = {
            'username': 'user_mailtest',
            'email': 'email@mail.com',
            'password': 'Password1'}
        User.objects.create_user(**self.credentials)
        user = User.objects.get(username='user_mailtest')
        user_pk = user.pk
        profile = Profile.objects.get(user_id=user_pk)
        profile.subscriptions.add(self.topic)
        profile.save()

    def get_mailinglist_test(self):
        mailinglist = get_mailing_list(self.topic.pk)
        self.assertIn("email@mail.com", mailinglist)
