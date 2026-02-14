from urllib import request
from django.shortcuts import render

from student.models import Student ,Parent
from django.db import transaction

from django.shortcuts import redirect
# Create your views here.
def addStudent(request):
     try:
            with transaction.atomic():

                # Parent creation
                parent = Parent.objects.create(
                    father_name=request.POST.get("father_name"),
                    mother_name=request.POST.get("mother_name"),
                    father_email=request.POST.get("father_email"),
                    mother_email=request.POST.get("mother_email"),
                    father_mobile=request.POST.get("father_mobile"),
                    mother_mobile=request.POST.get("mother_mobile"),
                    present_address=request.POST.get("present_address"),
                    permanent_address=request.POST.get("permanent_address"),
                )

                # Student creation
                student = Student.objects.create(
                    first_name=request.POST.get("first_name"),
                    last_name=request.POST.get("last_name"),
                    Student_id=request.POST.get("Student_id"),
                    date_of_birth=request.POST.get("date_of_birth"),
                    religion=request.POST.get("religion"),
                    mobile_number=request.POST.get("mobile_number"),
                    student_class=request.POST.get("student_class"),
                    section=request.POST.get("section"),
                    joining_date=request.POST.get("joining_date"),
                    admission_number=request.POST.get("admission_number"),
                    student_image=request.FILES.get("student_image"),
                    parent=parent,
                )

            return redirect("student_list")
     except Exception as e:
          print(f"Error occurred: {e}")
     return render(request,"Students/add-student.html")

def studentsList(request):
        student=Student.objects.select_related('parent').all()
        context={
            "students":student
        }
        return render(request,"Students/students.html",context)