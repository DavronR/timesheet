from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import datetime
from datetime import timedelta 

# Create your models here.

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)

class Location(models.Model):
    name = models.CharField(max_length=200)
    sector = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class HourCode(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    
class Activity(models.Model):
    work_date = models.DateField()
    location = models.ForeignKey(Location, related_name="location", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="activities", on_delete=models.CASCADE)
    time_in = models.TimeField()
    time_out = models.TimeField() 
    hour_code = models.ForeignKey(HourCode, related_name="hour_code", on_delete=models.CASCADE)
    fbp_payrol = models.DecimalField(max_digits=10, decimal_places=2)
    amco_payrol = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    def is_locked(self):
        today = timezone.now()
        if (today-self.created).days >= 45:
            return True 
        return False 
    
    def hours_worked(self):
        start = timedelta(hours=self.time_in.hour, minutes=self.time_in.minute)
        end = timedelta(hours=self.time_out.hour, minutes=self.time_out.minute)
        td = end - start
        days, hours, minutes = td.days, td.seconds // 3600, td.seconds // 60 % 60
        return f"{hours} hours and {minutes} minutes"


















    
    