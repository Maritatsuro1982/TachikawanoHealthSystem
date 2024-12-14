from django.db import models

class Member(models.Model):
    firstnamae=models.CharField(max_length=30)
    lastnamae=models.CharField(max_length=30)
    middlenamae=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    okaasan=models.CharField(max_length=30)
    otosan=models.CharField(max_length=30)
    birthplace=models.CharField(max_length=30)
    birthdate=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    denwa=models.CharField(max_length=30)
    denwa=models.CharField(max_length=30)
    nbs=models.CharField(max_length=30)
    blood_type=models.CharField(max_length=10)
 
    def __str__(self):
        return self.firstnamae + " " + self.lastnamae
   
  
    class Meta:  
        db_table = "web_member"


