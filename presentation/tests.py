from django.test import TestCase
from django.urls import reverse


class IndexPageTestCase(TestCase):

    # test that index returns a 200
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class ContactPageTestCase(TestCase):

    # test that contact returns a 200
    def test_contact_page(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)


class CovidinfoPageTestCase(TestCase):

    # test that covidinfo (named infocovid in url ... idk why) returns a 200
    def test_infocovid_page(self):
        response = self.client.get(reverse('infocovid'))
        self.assertEqual(response.status_code, 200)


class StagesPageTestCase(TestCase):

    # test that stages returns a 200
    def test_stages_page(self):
        response = self.client.get(reverse('stages'))
        self.assertEqual(response.status_code, 200)


class TeamPageTestCase(TestCase):

    # test that equipe returns a 200
    def test_team_page(self):
        response = self.client.get(reverse('equipe'))
        self.assertEqual(response.status_code, 200)


class PlanningPageTestCase(TestCase):

    # test that planning-et-tarifs returns a 200
    def test_Planning_page(self):
        response = self.client.get(reverse('planning-et-tarifs'))
        self.assertEqual(response.status_code, 200)


class MediaPageTestCase(TestCase):

    # test that medias returns a 200
    def test_media_page(self):
        response = self.client.get(reverse('medias'))
        self.assertEqual(response.status_code, 200)


class RentPageTestCase(TestCase):

    # test that location_salle returns a 200
    def test_rent_page(self):
        response = self.client.get(reverse('location_salle'))
        self.assertEqual(response.status_code, 200)


class LegalPageTestCase(TestCase):

    # test that legal returns a 200
    def test_legal_page(self):
        response = self.client.get(reverse('mentions-legales'))
        self.assertEqual(response.status_code, 200)
