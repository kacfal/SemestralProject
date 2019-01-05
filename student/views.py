from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Student
from .form import StudentModelForm
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
    DetailView
)


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


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
