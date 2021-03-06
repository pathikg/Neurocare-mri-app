
import datetime
from email import message
from django.db import models
from django.utils import timezone
from users.models import Profile

# Create your models here.
class doctor(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

class patient(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    disease = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Name

class lab(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    def __str__(self):
        return self.Name

class lab_report(models.Model):
    created_at = models.DateTimeField(default= timezone.now)
    lab= models.ForeignKey(Profile, on_delete=models.CASCADE , limit_choices_to={'category':'Lab_user'})
    patient = models.ForeignKey(Profile, on_delete=models.CASCADE , limit_choices_to={'category':'Patient'},related_name='Patient')
    doctor = models.ForeignKey(Profile, on_delete=models.CASCADE , limit_choices_to={'category':'Doctor'},related_name='Doctor')
    report_img = models.FileField(upload_to='report_img/', default='default.png')
    segment_img = models.FileField(upload_to='report_img/', default='default.png')
    report_summary = models.CharField(max_length=500)
    medicines = models.CharField(max_length=500)
    Mark_as_seen=models.BooleanField(default=False)
    def __str__(self):
        return self.patient.user.username


class appointment(models.Model):
    patient = models.ForeignKey(Profile, on_delete=models.CASCADE , default=0)
    department = models.CharField(max_length=500)
    doctor = models.CharField(max_length=500)
    message = models.CharField(max_length=500)
    date = models.DateField()
    seen=models.BooleanField(default=False)
    def __str__(self):
        return self.patient.user.username

    


