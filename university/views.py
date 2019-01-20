from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveAPIView
from .models import University
from .serializers import UniversitySerializer


class UniversityListAPIView(ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class UniversityDeleteAPIView(DestroyAPIView):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()
    lookup_field = 'id'


class UniversityDetailsAPIView(RetrieveAPIView):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()
    lookup_field = 'id'
