from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    StudentCreateView,
    StudentDeleteView,
    StudentDetailView,
    StudentListView,
    StudentUpdateView,
    # StudentListCreateAPIView,
    StudentDetailAPIView,
    StudentDeleteAPIView,
)


app_name = 'student'
urlpatterns = [
    path('', StudentListView.as_view(),  name='student-list'),
    path('<int:id>/', StudentDetailView.as_view(), name='student-details'),
    path('create/', StudentCreateView.as_view(),  name='student-create'),
    path('<int:id>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('<int:id>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    # path('api/', StudentListCreateAPIView.as_view(), name='student-api-list-create'),
    path('api/<int:student_id>', StudentDetailAPIView.as_view(), name='student-api-detail'),
    path('api/<int:student_id>/delete', StudentDeleteAPIView.as_view(), name='student-api-delete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
