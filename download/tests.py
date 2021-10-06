from django.test import TestCase
from django.urls import reverse
from django.core.files import File
from django.utils import timezone

import mock

from .models import Downloadable


class DownloadTest(TestCase):

    def setUp(self):
        self.file_mock = mock.MagicMock(spec=File)
        self.file_mock.name = 'test.pdf'
        Downloadable.objects.create(
            name=self.file_mock.name,
            file=self.file_mock,
            date_uploaded=timezone.now())
        self.test_file = Downloadable.objects.get(name="test.pdf")

    def test_download_page(self):
        """Checks if file set up is in context[download links]"""
        response = self.client.get(reverse('documents'))
        self.assertIn(self.test_file, response.context['download_links'])
