from rest_framework.generics import ListCreateAPIView, DestroyAPIView

from .models import University
from .serializers import UniversitySerializer


class UniversityListCreateAPIView(ListCreateAPIView):
    serializer_class = UniversitySerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        _id = self.kwargs.get("id")
        return University.objects.all()


class UniversityDeleteAPIView(DestroyAPIView):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()
    lookup_field = 'university_id'
