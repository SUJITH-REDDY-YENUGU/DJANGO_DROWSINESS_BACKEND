from django.db import models

# Create your models here.
class Bus(models.Model):
    registration_number=models.CharField(max_length=50)
    start_location=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    camera_id=models.CharField(max_length=50)

class Driver(models.Model):
    name=models.CharField(max_length=100)
    license_number=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    assigned_bus=models.ForeignKey(Bus,on_delete=models.SET_NULL,null=True)
    total_drowsies=models.IntegerField(default=0)

class DrowsinessEvent(models.Model):
    driver=models.ForeignKey(Driver,on_delete=models.CASCADE)
    bus=models.ForeignKey(Bus,on_delete=models.CASCADE)
    timestamp=models.DateTimeField()
    current_location=models.CharField(max_length=100)