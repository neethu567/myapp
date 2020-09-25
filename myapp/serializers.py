from rest_framework import serializers
from .models import Scholl,Subject,Student

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields=['id', 'subject_name']

class SchoolSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=True)
    class Meta:
        model=Scholl
        fields=['id', 'school_Names','school_adress','subject']

class StudentSerializer(serializers.ModelSerializer):
    school=SchoolSerializer()
    class Meta:
        model=Student
        fields=['id', 'student_names','mobile_number','alternate_number','school']

class SubjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields = ['id', 'subject_name']

class SchoolCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Scholl
        fields=['id', 'school_Names','school_adress','subject']

class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id', 'student_names','mobile_number','alternate_number','school']
