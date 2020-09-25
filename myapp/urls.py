from django.urls import path
from .import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('subject/', views.SubjectList.as_view()),
    path('subject/<int:pk>/', views.SubjectDetail.as_view()),
    path('school/', views.SchoolList.as_view()),
    path('school/<int:pk>/', views.SchoolDetail.as_view()),
    path('student/', views.StudentList.as_view()),
    path('student/<int:pk>/', views.StudentDetail.as_view()),
    # path('schoolview/', views.schoolviewList.as_view()),
    # path('schoolview/<int:pk>/', views.schoolviewDetail.as_view()),
    # path('studentview/', views.studentviewList.as_view()),
    # path('studentview/<int:pk>/', views.studentviewDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)