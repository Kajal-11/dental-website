from django.db import models
import datetime
# Create your models here.
class Appointment(models.Model):
    first_name = models.CharField(max_length = 50,null = True,blank = True,default='')
    last_name = models.CharField(max_length = 50,null = True,blank = True,default='')
    phone = models.CharField(max_length = 150,null = True,blank = True,default='')
    date = models.CharField(max_length = 150,null = True,blank = True,default='')
    message = models.CharField(max_length = 200,null = True,blank = True,default='')