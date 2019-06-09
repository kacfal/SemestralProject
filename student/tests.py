from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.reverse import reverse

from student.models import Student
from student.serializers import StudentSerializer

from university.models import University


class StudentTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        university_id = University.objects.create(
            name="Polibuda",
            abbreviation='Pwr',
            city='Wroclaw'

        )

        Student.objects.create(
            university_id=university_id,
            department='W4',
            profile='telkomunkacja',
            name='Jan',
            last_name='Kowalski',
            index=123456,
            status='Active',
            deficit=10
        )
        self.student = Student.objects.create(
            university_id=university_id,
            department='W4',
            profile='telkomunkacja',
            name='Jan1',
            last_name='Kowalski2',
            index=123456,
            status='Inactive',
            deficit=10
        )
        self.valid_payload = {
            'department': 'W4',
            'profile': 'telkomunkacja',
            'name': 'Jan1',
            'last_name': 'Kowalski2',
            'index': 123456,
            'status': 'Inactive',
            'deficit': 10
        }

        self.invalid_payload = {}

    def test_get_list_student(self):
        response = self.client.get(
            reverse('student:api-list-create',
                    kwargs={'university_id': 0})
        )
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        self.assertEqual(len(students), 2)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_get_details_student(self):
        response = self.client.get(
            reverse('student:api-detail',
                    kwargs={
                        'id': 1
                    })
        )
        student = Student.objects.first()
        serializer = StudentSerializer(student)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_get_details_student(self):
        response = self.client.get(
            reverse('student:api-detail',
                    kwargs={
                        'id': 0
                    })
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_create_student(self):
        response = self.client.post(
            reverse('student:api-list-create',
                    kwargs={
                        'university_id': 1
                    }),
            data=self.valid_payload
        )
        students = Student.objects.all()
        self.assertEqual(len(students), 3)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_create_student(self):
        response = self.client.post(
            reverse('student:api-list-create',
                    kwargs={
                        'university_id': 1
                    }),
            data=self.invalid_payload
        )
        students = Student.objects.all()
        self.assertEqual(len(students), 2)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_student(self):
        response = self.client.delete(
            reverse('student:api-delete',
                    kwargs={
                        'id': 1
                    })
        )
        students = Student.objects.all()
        self.assertEqual(len(students), 1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_student(self):
        response = self.client.delete(
            reverse('student:api-delete',
                    kwargs={
                        'id': 0
                    })
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_update_student(self):
        response = self.client.put(
            reverse('student:api-update',
                    kwargs={
                        'id': 1
                    }),
            data=self.valid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_student(self):
        response = self.client.put(
            reverse('student:api-update',
                    kwargs={
                        'id': 1
                    }),
            data=self.invalid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
