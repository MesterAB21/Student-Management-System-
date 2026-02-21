from datetime import timedelta
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    
    is_authorized=models.BooleanField(default=False)

    Roles=(("student","student"),("teacher","teacher"),("admin","admin"))
    role=models.CharField(max_length=10,choices=Roles)

class PasswordRestRequest(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    token=models.CharField(max_length=100,editable=False,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)  
    Token_validity=models.DurationField(default=timedelta(hours=1))  
    def isvalid(self):
        return self.created_at + self.Token_validity > timezone.now()
    def send_password_reset_email(self):
        reset_link = f"http://localhost:8000/auth/reset-password/{self.token}/"
        send_mail(
        subject="Password Reset Request",
        message=f"  Click the link to reset your password in your school Account: {reset_link}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[self.user.email],
        fail_silently=False,
    )