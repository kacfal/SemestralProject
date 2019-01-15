from rest_framework import serializers
from .models import Student, University


class StudentSerializer(serializers.ModelSerializer):
    """
    Todo:
    Add university to api
    """
    class Meta:
        model = Student
        fields = '__all__'
        depth = 2


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'
