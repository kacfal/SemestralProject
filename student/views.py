from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Student
from .form import StudentModelForm
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
    DetailView,
)
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


@csrf_exempt
def student_api_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def student_api_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=204)


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
