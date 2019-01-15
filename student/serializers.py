from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    """
    Todo:
    Add university to api
    """
    class Meta:
        model = Student
        fields = '__all__'
        depth = 2
