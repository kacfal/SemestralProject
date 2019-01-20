from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    StudentCreateView,
    StudentDeleteView,
    StudentDetailView,
    StudentListView,
    StudentUpdateView,
    StudentListCreateAPIView,
    StudentDetailsDeleteAPIView,
)


app_name = 'student'
urlpatterns = [
    path('', StudentListView.as_view(),  name='list'),
    path('<int:id>/', StudentDetailView.as_view(), name='details'),
    path('create/', StudentCreateView.as_view(),  name='create'),
    path('<int:id>/update/', StudentUpdateView.as_view(), name='update'),
    path('<int:id>/delete/', StudentDeleteView.as_view(), name='delete'),
    path('api/<int:university_id>', StudentListCreateAPIView.as_view(), name='api-list-create'),
    path('api/detail/<int:id>', StudentDetailsDeleteAPIView.as_view(), name='api-detail-delete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
