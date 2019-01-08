from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    StudentCreateView,
    StudentDeleteView,
    StudentDetailView,
    StudentListView,
    StudentUpdateView,
    StudentAPIListView,
    StudentAPIDetailView
)


app_name = 'student'
urlpatterns = [
    path('', StudentListView.as_view(),  name='student-list'),
    path('<int:id>/', StudentDetailView.as_view(), name='student-details'),
    path('create/', StudentCreateView.as_view(),  name='student-create'),
    path('<int:id>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('<int:id>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    path('api/', StudentAPIListView.as_view(), name='student-api-list'),
    path('api/<int:pk>', StudentAPIDetailView.as_view(), name='student-api-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
