from django.urls import path
from django.urls import include

from student import views
urlpatterns = [
   path("add/",views.addStudent,name="add_student"),
   path('',views.studentsList,name="Students-list"),
   path('<slug:slug>/edit/',views.edit_student,name="edit_student"),
   path('<slug:slug>/',views.student_details,name="student_details"),
   path('<slug:slug>/delete/',views.delete_student,name="delete_student"),
]