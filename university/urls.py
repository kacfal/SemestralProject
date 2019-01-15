from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    UniversityDeleteAPIView,
    UniversityListCreateAPIView

)


app_name = 'university'
urlpatterns = [
    path('university/', UniversityListCreateAPIView.as_view(), name='university-api-list-create'),
    path('university/<int:university_id>/delete', UniversityDeleteAPIView.as_view(), name='university-api-delete')
]

urlpatterns = format_suffix_patterns(urlpatterns)
