from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient

from planetarium_api.models import PlanetariumDome
from planetarium_api.serializers import PlanetariumDomeSerializer

URL = reverse("planetarium_api:planetariumdome-list")


def detail_url(dome_id: int) -> str:
    return reverse("planetarium_api:planetariumdome-detail", args=[dome_id])


def create_planetarium_dome(**params) -> PlanetariumDome:
    defaults = {
        "name": "test",
        "rows": 10,
        "seats_in_row": 10,
    }
    defaults.update(params)

    return PlanetariumDome.objects.create(**defaults)


class UnauthenticatedPlanetariumDomeTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(URL)
        self.assertEquals(res.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedPlanetariumDomeTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test@test.com",
            "testpass",
        )
        self.client.force_authenticate(self.user)

    def test_list_domes(self):
        create_planetarium_dome()
        create_planetarium_dome()

        res = self.client.get(URL)

        domes = PlanetariumDome.objects.all()
        serializer = PlanetariumDomeSerializer(domes, many=True)

        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertEquals(res.data, serializer.data)

    def test_retrieve_dome_detail(self):
        dome = create_planetarium_dome()

        url = detail_url(dome.id)
        res = self.client.get(url)

        serializer = PlanetariumDomeSerializer(dome)

        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertEquals(res.data, serializer.data)

    def test_create_dome_forbidden(self):
        payload = {
            "name": "test",
            "rows": 11,
            "seats_in_row": 20,
        }

        res = self.client.post(URL, data=payload)

        self.assertEquals(res.status_code, status.HTTP_403_FORBIDDEN)


class AdminPlanetariumDomeTests (TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "admin@admin.com",
            "testpass",
            is_staff=True,
        )

        self.client.force_authenticate(self.user)

    def test_create_bus(self):
        payload = {
            "name": "test",
            "rows": 10,
            "seats_in_row": 10,
        }

        res = self.client.post(URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
