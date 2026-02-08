from django.db import models
from django.utils import timezone

# Create your models here.

class AppVariety(models.Model):
    APP_TYPE_CHOICES = [
        ('AI','Artificial Intelligence'),
        ('ML','Machine Learning'),
        ('GA','Generative AI'),
        ('AA','Agentic AI'),
    ]

    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='apps')
    date_added=models.DateTimeField(default=timezone.now) 
    type=models.CharField(max_length=2, choices=APP_TYPE_CHOICES)