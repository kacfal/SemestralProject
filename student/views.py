from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView

from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView

from .models import Student
from .form import StudentModelForm
from .serializers import StudentSerializer

from university.models import University


class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # def perform_create(self, serializer):
    #     university_obj = get_object_or_404(University, id=self.kwargs['university_id'])
    #     serializer.save(
    #         university_id=university_obj
    #     )


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


class StudentCreateView(CreateView):
    template_name = 'student_create.html'
    form_class = StudentModelForm
    queryset = Student.objects.all()

    def get_success_url(self):
        return '/student'

    def form_valid(self, form):
        return super().form_valid(form)


class StudentDeleteView(DeleteView):
    template_name = 'student_delete.html'

    def get_object(self, queryset=None):
        _id = self.kwargs.get("id")
        return get_object_or_404(Student, id=_id)

    def get_success_url(self):
        return reverse('student:student-list')


class StudentDetailView(DetailView):
    template_name = 'student_details.html'

    def get_object(self, queryset=None):
        _id = self.kwargs.get('id')
        return get_object_or_404(Student, id=_id)


class StudentListView(ListView):
    template_name = 'student_list.html'
    queryset = Student.objects.all()


class StudentUpdateView(UpdateView):
    template_name = 'student_create.html'
    form_class = StudentModelForm

    def get_object(self, queryset=None):
        _id = self.kwargs.get("id")
        return get_object_or_404(Student, id=_id)

    def get_success_url(self):
        return '/student'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
