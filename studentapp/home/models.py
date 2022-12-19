from django.db import models

# Create your models here.
class Student(models.Model):
    student_id =models.AutoField(primary_key=True)
    stud_name=models.CharField(max_length=30)
    stud_phone=models.CharField(max_length=10)
    stud_email=models.EmailField(max_length=100)
    stud_address=models.CharField(max_length=100)
    stud_place=models.CharField(max_length=100)
    