from django.urls import path
from django.urls import include

from student import views
urlpatterns = [
   path("add/",views.addStudent,name="add_student"),
   path('',views.studentsList,name="Students-list"),
]