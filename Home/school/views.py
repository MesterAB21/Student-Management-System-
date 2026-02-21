from django.shortcuts import render
from django.http import HttpResponse
from student.models import Student
from AuthHome.models import CustomUser
from school.models import Notification
# Create your views here.
def index(request):
    total_students = Student.objects.count()
    total_users = CustomUser.objects.count()
    recent_students = Student.objects.select_related('parent').order_by('-joining_date')[:5]
    context = {
        "total_students": total_students,
        "total_users": total_users,
        "recent_students": recent_students,
    }
    return render(request, "Home/index.html", context)

def dashboard(request):
    total_students = Student.objects.count()
    context = {
        "total_students": total_students,
    }
    return render(request, "Students/student-dashboard.html", context)