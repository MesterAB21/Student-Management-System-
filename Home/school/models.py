import uuid

from django.db import models

# Create your models here.
class Notification(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user=models.ForeignKey("AuthHome.CustomUser",on_delete=models.CASCADE)
    message=models.TextField()
    is_read=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message
    