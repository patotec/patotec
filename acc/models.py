
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from PIL import Image




class CustomUser(AbstractUser):
    sex_choices = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
    )
    STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    )
    phone = models.IntegerField(default='0')
    country = models.CharField(max_length=50, default='')
    salary = models.CharField(max_length=500,default='')
    sex = models.CharField(max_length=10, choices=sex_choices, default='')
    occupation = models.CharField(max_length=200,blank=True)
    message = models.TextField(max_length=2000,blank=True)
    active = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')
    image = models.ImageField(default='default.jpg')
    def __str__(self):
        return self.username


    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

# class Profile(models.Model):

    
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg')
  

    
   



#     def __str__(self):
#         return f'{self.user.username} Profile'



	
# Create your models here.
