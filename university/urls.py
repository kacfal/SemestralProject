from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    UniversityDeleteAPIView,
    UniversityListAPIView,
    UniversityDetailsAPIView

)


app_name = 'university'
urlpatterns = [
    path('', UniversityListAPIView.as_view(), name='api-list'),
    path('delete/<int:id>/', UniversityDeleteAPIView.as_view(), name='api-delete'),
    path('details/<int:id>/', UniversityDetailsAPIView.as_view(), name='api-details')
]

urlpatterns = format_suffix_patterns(urlpatterns)
