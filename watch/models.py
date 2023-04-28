from datetime import timezone
from django.utils import timezone
from django.db import models
import django.utils.timezone

# Create your models here.
class activity(models.Model):
    name= models.CharField(max_length=100)
    total_time = models.CharField(max_length=50)
    pc_id = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    
class myuser(models.Model):
    email=models.CharField(max_length=100)
    username=models.CharField(max_length=100)


 