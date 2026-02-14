from django.db import models

from django.utils.text import slugify
# Create your models here.
class Parent(models.Model):
    father_name=models.CharField(max_length=50)
    mother_name=models.CharField(max_length=50)
    father_email=models.EmailField()
    mother_email=models.EmailField()
    father_mobile=models.CharField(max_length=15)
    mother_mobile=models.CharField(max_length=15)
    present_address=models.TextField()
    permanent_address=models.TextField()
    def __str__(self):
        return f'{self.father_name} & {self.mother_name}'



class Student(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    Student_id=models.CharField(max_length=20,unique=True)
    gender=models.CharField(max_length=10 ,choices=[('Male','Male'),('Female','Female')])
    date_of_birth=models.DateField()
    religion=models.CharField(max_length=20)
    mobile_number=models.CharField(max_length=15)
    student_class=models.CharField(max_length=20)
    section=models.CharField(max_length=20)
    joining_date=models.DateField()
    admission_number=models.CharField(max_length=20,unique=True)
    student_image=models.ImageField(upload_to='students/',blank=True)
    parent=models.OneToOneField(Parent,on_delete=models.CASCADE)
    slug=models.SlugField(unique=True,blank=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.Student_id}'
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(f"{self.first_name}-{self.last_name}-{self.Student_id}")
        super(Student,self).save(*args,**kwargs)