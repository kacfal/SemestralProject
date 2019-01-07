from django.urls import path
from .views import (
    StudentCreateView,
    StudentDeleteView,
    StudentDetailView,
    StudentListView,
    StudentUpdateView,
    student_api_detail,
    student_api_list
)


app_name = 'student'
urlpatterns = [
    path('', StudentListView.as_view(),  name='student-list'),
    path('<int:id>/', StudentDetailView.as_view(), name='student-details'),
    path('create/', StudentCreateView.as_view(),  name='student-create'),
    path('<int:id>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('<int:id>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    path('api/', student_api_list),
    path('api/<int:pk>', student_api_detail)
]
