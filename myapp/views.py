from .models import Subject,Scholl,Student
# from .serializers import SubjectSerializer,SchoolSerializer,StudentSerializer,SchoolviewSerializer,StudentviewSerializer
from rest_framework import generics
from .serializers import SubjectSerializer,SchoolSerializer,StudentSerializer,SubjectCreateSerializer,SchoolCreateSerializer,StudentCreateSerializer


class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    # serializer_class = SubjectSerializer

    def get_serializer_class(self):
        if self.request.method in["PATCH","PUT","POST"]:
            return SubjectSerializer
        return SubjectCreateSerializer

class SchoolList(generics.ListCreateAPIView):
    queryset = Scholl.objects.all()
    serializer_class = SchoolSerializer


class SchoolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scholl.objects.all()
    # serializer_class = SchoolSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return SchoolCreateSerializer
        return SchoolSerializer


class StudentList(generics.ListCreateAPIView):
    queryset =Student.objects.all()
    serializer_class = StudentSerializer
    def get_serializer_class(self):
        if self.request.method == "POST":
            return StudentCreateSerializer
        return StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    # serializer_class = StudentSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return StudentCreateSerializer
        return StudentSerializer