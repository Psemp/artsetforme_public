# from django.test import TestCase
# from backoffice.models import Topic
# from django.utils import timezone
# from django.urls import reverse

# from .models import Blogpost


# class BlogTest(TestCase):

#     def setUp(self):
#         self.category_1_info = {
#             'name': 'topic1',
#             }
#         Topic.objects.create(**self.category_1_info)

#         self.category_2_info = {
#             'name': 'topic2',
#             }
#         Topic.objects.create(**self.category_2_info)

#         self.category_3_info = {
#             'name': 'topic3',
#             }
#         Topic.objects.create(**self.category_3_info)

#         self.blogpost1_data = {
#             'category': Topic.objects.get(name='topic1'),
#             'title': "bp1",
#             'content': 'some content',
#             'date_posted': timezone.now()
#             }
#         Blogpost.objects.create(**self.blogpost1_data)

#         self.blogpost2_data = {
#             'category': Topic.objects.get(name='topic2'),
#             'title': "bp2",
#             'date_posted': timezone.now()
#             }
#         Blogpost.objects.create(**self.blogpost2_data)

#     def test_blogpost_test(self):
#         response = self.client.get(reverse('blog:actualites'))
#         print(response.context['object_list'])
#         self.assertIn(Blogpost.objects.get(title="bp1"), response.context['object_list'])
#         self.assertIn(Blogpost.objects.get(title="bp2"), response.context['object_list'])
