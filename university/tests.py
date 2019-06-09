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
            abbreviation='Pwr',
            city='Wroclaw',

        )

        self.university = University.objects.create(
            name="2Polibuda",
            abbreviation='2Pwr',
            city='Wroclaw',
        )

        self.valid_payload = {
            "city": 'Wroclaw',
            'name': 'Great Polibuda',
            'abbreviation': 'Gr Pwr'
        }

        self.invalid_payload = {}

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
            data=self.valid_payload
        )
        universities = University.objects.all()
        self.assertEqual(len(universities), 3)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_create_unique_university(self):
        unique_university = {
            "city": 'Wroclaw',
            'name': 'Polibuda',
            'abbreviation': 'Pwr'
        }

        response = self.client.post(
            reverse('university:api-list'),
            data=unique_university
        )
        universities = University.objects.all()
        self.assertEqual(len(universities), 2)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_create_university(self):
        response = self.client.post(
            reverse('university:api-list'),
            data=self.invalid_payload
        )
        universities = University.objects.all()
        self.assertEqual(len(universities), 2)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_university(self):
        response = self.client.delete(
            reverse('university:api-delete',
                    kwargs={
                        'id': 1
                    })
        )
        universities = University.objects.all()
        self.assertEqual(len(universities), 1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_university(self):
        response = self.client.delete(
            reverse('university:api-delete',
                    kwargs={
                        'id': 0
                    })
        )
        universities = University.objects.all()
        self.assertEqual(len(universities), 2)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_update_university(self):
        response = self.client.put(
            reverse('university:api-update',
                    kwargs={
                        'id': 1
                    }),
            data=self.valid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_university(self):
        response = self.client.put(
            reverse('university:api-update',
                    kwargs={
                        'id': 1
                    }),
            data=self.invalid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)