from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.reverse import reverse

from university.models import University
from university.serializers import UniversitySerializer


class UniversityTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        University.objects.create(
            name="Polibuda",
            abbreviation='Pwr'
        )
        self.university = University.objects.create(
            name="2Polibuda",
            abbreviation='2Pwr'
        )
        self.valid_create_payload = {
            'name': 'Great Polibuda',
            'abbreviation': 'Gr Pwr'
        }

    def test_get_list_university(self):
        response = self.client.get(
            reverse('university:api-list')
        )
        universities = University.objects.all()
        serializer = UniversitySerializer(universities, many=True)
        self.assertEqual(len(universities), 2)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_get_details_university(self):
        response = self.client.get(
            reverse('university:api-details',
                    kwargs={
                        'id': 1
                    })
        )
        university = University.objects.first()
        serializer = UniversitySerializer(university)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_get_details_university(self):
        response = self.client.get(
            reverse('university:api-details',
                    kwargs={
                        'id': 0
                    })
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_create_university(self):
        response = self.client.post(
            reverse('university:api-list'),
            data={
                'name': 'Great Polibuda',
                'abbreviation': 'Gr Pwr'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_create_university(self):
        response = self.client.post(
            reverse('university:api-list'),
            data={}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_university(self):
        response = self.client.delete(
            reverse('university:api-delete',
                    kwargs={
                        'id': 1
                    })
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_university(self):
        response = self.client.delete(
            reverse('university:api-delete',
                    kwargs={
                        'id': 0
                    })
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
