from django.contrib.auth.backends import ModelBackend
from AuthHome.models import CustomUser
from school.models import Notification


class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None
    

def create_notification(user, message):
    Notification.objects.create(
        user=user,
        message=message
    )    
