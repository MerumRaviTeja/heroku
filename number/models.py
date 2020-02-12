from django.db import models
class data(models.Model):
    Enter_Name=models.CharField(max_length=20)
    Securitycode=models.CharField(max_length=20)
    Score=models.IntegerField(default=0)
    Email_Address=models.EmailField()