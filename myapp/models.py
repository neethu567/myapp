# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Subject(models.Model):
    subject_name=models.TextField(max_length=200)

    class Meta:
        ordering = ['subject_name']

class Scholl(models.Model):
    school_Names=models.CharField(max_length=50)
    school_adress=models.TextField(max_length=500)
    subject=models.ManyToManyField(Subject)

    class Meta:
        ordering = ['school_Names']

class Student(models.Model):
    student_names=models.CharField(max_length=300)
    mobile_number=models.IntegerField()
    alternate_number=models.IntegerField()
    school=models.ForeignKey(Scholl,on_delete=models.CASCADE,null=True)

    class Meta:
        ordering = ['student_names']


