from django.db import models

from django.contrib.auth.models import User 
from django.utils import timezone


class UserFile(models.Model): 
    file = models.FileField(upload_to='uploads/') 
   
class UserResults(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=400)
    result = models.TextField()
    generated_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Result for {self.file_name} by {self.user}"
    
class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    file_name = models.CharField(max_length=455)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    total_rows= models.IntegerField(default=0)
    total_columns  = models.IntegerField(default=0)
      
   
    
    
