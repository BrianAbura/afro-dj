from django.db import models

# Create your models here.
# Creating Custom Model: Members
class Members(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=255)
    password_repeat = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now=True) 