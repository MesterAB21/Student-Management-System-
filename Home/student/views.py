from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render


from AuthHome.backends import create_notification
from student.models import Student ,Parent
from django.db import transaction

from django.shortcuts import redirect
# Create your views here.
@login_required(login_url="login")
def student_details(request,slug):
     student=get_object_or_404(Student,slug=slug)
     context={
          "student":student
     }
     return render(request,"Students/student-details.html",context)




from django.db import transaction
from django.shortcuts import render, redirect

@login_required(login_url="login")
def addStudent(request):
    try:
        if request.method == "POST":
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
                    gender=request.POST.get("gender"),
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
                messages.success(request, "Student added successfully.")
                create_notification(request.user,f"Student {student.first_name} {student.last_name} has been added.")
            return redirect("Students-list")

        return render(request, "Students/add-student.html")

    except Exception as e:
        print(f"Error occurred: {e}")
        return render(request, "Students/add-student.html")


@login_required(login_url="login")
def studentsList(request):
        student=Student.objects.select_related('parent').all()
        context={
            "students":student
        }
        return render(request,"Students/students.html",context)
@login_required(login_url="login")
def edit_student(request,slug):
      student=get_object_or_404(Student,slug=slug)
      parent=student.parent if hasattr(student,'parent') else None
      if request.method=="POST":
            try:
                    if parent:
                        parent.father_name=request.POST.get("father_name")
                        parent.mother_name=request.POST.get("mother_name")
                        parent.father_email=request.POST.get("father_email")
                        parent.mother_email=request.POST.get("mother_email")
                        parent.father_mobile=request.POST.get("father_mobile")
                        parent.mother_mobile=request.POST.get("mother_mobile")
                        parent.present_address=request.POST.get("present_address")
                        parent.permanent_address=request.POST.get("permanent_address")
                        parent.save()
                    student.first_name=request.POST.get("first_name")
                    student.last_name=request.POST.get("last_name")
                    student.Student_id=request.POST.get("Student_id")
                    student.gender=request.POST.get("gender")
                    student.date_of_birth=request.POST.get("date_of_birth")
                    student.religion=request.POST.get("religion")
                    student.mobile_number=request.POST.get("mobile_number")
                    student.student_class=request.POST.get("student_class")
                    student.section=request.POST.get("section")
                    student.joining_date=request.POST.get("joining_date")
                    student.admission_number=request.POST.get("admission_number")
                    if request.FILES.get("student_image"):
                         student.student_image=request.FILES.get("student_image") 
                    student.save()
                    messages.success(request, "Student updated successfully.")
                    create_notification(request.user,f"Student {student.first_name} {student.last_name} has been updated.")
                    return redirect("Students-list") 
            except Exception as e:
             print(f"Error occurred: {e}")
             student.refresh_from_db()
             
      return render(request,"Students/edit-student.html",{"student":student})
                                                                
@login_required(login_url="login")
def delete_student(request,slug):
      student=get_object_or_404(Student,slug=slug)
      if request.method=="POST":
            student.delete()
            create_notification(request.user,f"Student {student.first_name} {student.last_name} has been deleted.")
            return redirect("Students-list")
      return HttpResponseForbidden("You are not allowed to delete this student.")
     