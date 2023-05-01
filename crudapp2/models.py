from django.db import models

# Create your models here.
class Patient(models.Model):
    p_id = models.IntegerField()
    p_name = models.CharField(max_length=100)
    p_age = models.IntegerField()
    p_gender = models.CharField(max_length=20)
    p_dob = models.DateField()
    p_phone = models.CharField(max_length=20)
    
    def __str__(self):
        return(f"{self.p_id}---{self.p_name}---{self.p_age}")
