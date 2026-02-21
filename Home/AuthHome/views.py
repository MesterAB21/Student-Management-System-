from django.contrib import messages
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import redirect, render
from django.db import transaction
from django.contrib.auth import login,logout
from django.contrib.auth.tokens import default_token_generator
from AuthHome.models import CustomUser, PasswordRestRequest
from django.contrib.auth import authenticate

from school.models import Notification
# Create your views here.
def SignUp(request):
    
    if request.method=="POST":
        try:
            with transaction.atomic():
                 user=CustomUser.objects.create_user(
                 username=request.POST.get("username"),
                 password=request.POST.get("password"),
                 email=request.POST.get("email"),
                 role=request.POST.get("role")
                      )
                
                 login(request,user)
                 messages.success(request,"User created successfully")
                 if user.role=="admin":
                    return redirect("admin-dashboard")  
                 elif user.role=="teacher":
                    return redirect("teacher-dashboard")
                 elif user.role=="student":
                    return redirect("dashboard")    
        except Exception as e:
            print(e)
    return render(request,"AuthHome/signup.html") 

def SignIn(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in successfully")
            if user.role=="admin":  
                return redirect("admin-dashboard")
            elif user.role=="teacher":
                return redirect("teacher-dashboard")
            else:
                return redirect("dashboard")
        else:
            messages.error(request,"Invalid email or password")       
    return render(request,"AuthHome/login.html")


def forget_password(request):
    if request.method=="POST":
        email=request.POST.get("email")
        user=CustomUser.objects.filter(email=email).first()
        if user:
            token=default_token_generator.make_token(user)
            reset_request=PasswordRestRequest.objects.create(user=user,token=token)
            reset_request.send_password_reset_email()
            messages.success(request,"Password reset instructions sent to your email.")
        else:
            messages.error(request,"No user found with this email.")
    return render(request,"AuthHome/forgot-password.html")


def logout_user(request):
    logout(request)
    return redirect("index")


def reset_password(request,token):
    reset_request=PasswordRestRequest.objects.filter(token=token).first()
    if not reset_request or not reset_request.isvalid():
        messages.error(request,"Invalid or expired token.")
        return redirect("forget-password")
    if request.method=="POST":
        new_password=request.POST.get("new_password")
        user=reset_request.user
        user.set_password(new_password)
        user.save()
        reset_request.delete()  
        messages.success(request,"Password reset successfully. You can now log in.")
        return redirect("login")          
    return render(request,"AuthHome/reset-password.html",{"token":token})


def mark_as_read(request):

    notification = Notification.objects.filter(user=request.user, is_read=False)
    notification.update(is_read=True)
    # Redirect back to previous page
    return redirect(request.META.get("HTTP_REFERER", "/"))
    



def clear_notifications(request):
    if request.method in ["POST", "GET"]:
        notifications = Notification.objects.filter(user=request.user)
        notifications.delete()
        return redirect(request.META.get("HTTP_REFERER", "/"))
    return HttpResponseForbidden("Invalid request method.")
    
        
          
