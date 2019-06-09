from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    StudentListCreateAPIView,
    StudentUpdateAPIView,
    StudentDeleteAPIView,
    StudentDetailsAPIView
)


app_name = 'student'
urlpatterns = [
    path('', StudentListCreateAPIView.as_view(), name='api-list-create'),
    path('detail/<int:id>', StudentDetailsAPIView.as_view(), name='api-detail'),
    path('delete/<int:id>', StudentDeleteAPIView.as_view(), name='api-delete'),
    path('update/<int:id>', StudentUpdateAPIView.as_view(), name='api-update')
]

urlpatterns = format_suffix_patterns(urlpatterns)
