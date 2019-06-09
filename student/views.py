from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView

from .models import Student
from .serializers import StudentSerializer


class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdateAPIView(UpdateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'id'


class StudentDetailsAPIView(RetrieveAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'id'


class StudentDeleteAPIView(DestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'id'

