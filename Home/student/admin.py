from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student,Parent
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'Student_id',  'section',"gender","mobile_number","admission_number","joining_date","student_class")
    search_fields = ('first_name', 'last_name', 'Student_id',  'student_class','admission_number')
    list_filter = ('student_class', 'section', 'gender')
    readonly_fields = ('student_image',)
@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
    search_fields = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
  