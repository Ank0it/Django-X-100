from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class AppVariety(models.Model):
    APP_TYPE_CHOICES = [
        ('AI','Artificial Intelligence'),
        ('ML','Machine Learning'),
        ('GA','Generative AI'),
        ('AA','Agentic AI'),
    ]

    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='apps/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=APP_TYPE_CHOICES)
    description=models.TextField(default='') 

    def __str__(self):
        return self.name
    
#  One to many

class AppReviews(models.Model):
    app = models.ForeignKey(AppVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.app.name}'

#  Many to Many 

class Store(models.Model):
     name = models.CharField(max_length=100 )
     location = models.CharField(max_length=100)
     app_varieties = models.ManyToManyField(AppVariety, related_name='stores')

     def __str__(self):
        return self.name
         
#  One to One

class AppCertificate(models.Model):
    app=models.OneToOneField(AppVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number= models.CharField(max_length=100)
    issued_date = models.DateField(default=timezone.now)
    valid_untill=models.DateField()

    def __str__(self):
        return f'Certificate for {self.app.name}'





    