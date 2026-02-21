from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path("signup/",views.SignUp,name="signup"),
    path("login/",views.SignIn,name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("forgot-password/",views.forget_password,name="forgot-password"),
    path("reset-password/<str:token>/",views.reset_password,name="reset-password"),
    path("mark-as-read/",views.mark_as_read,name="mark_as_read"),
    path("clear-notifications/",views.clear_notifications,name="clear_notifications"),
]