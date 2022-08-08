from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    
    Name=models.CharField(max_length=25)
    Department_head=models.CharField(max_length=20)

    def __str__(self):
        return self.Name
    class Meta:
        unique_together = ["Department_head"]

class Doctor(models.Model):

   Name=models.CharField(max_length=35)
   Department=models.ForeignKey(Department,on_delete=models.CASCADE) 
   Contact_number=models.IntegerField()
    
   def __str__(self):
        return self.Name
   class Meta:
        unique_together = ["Contact_number"]
   
class Patient(models.Model): 
   
    Name=models.CharField(max_length=100)
    Department=models.ForeignKey(Department,on_delete=models.CASCADE)
    contact_number=models.IntegerField()
    Doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.Name
    class Meta:
        unique_together = ["contact_number"]


