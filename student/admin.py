from django.contrib import admin
from .models import Student, University, Department, Profile

# Register your models here.
admin.site.register(Student)
admin.site.register(University)
admin.site.register(Department)
admin.site.register(Profile)

