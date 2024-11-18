from django.db import models
from django.contrib.auth.models import User 

# Create your models here.



class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Messaged by {self.user}"

    