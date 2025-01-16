from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    message=models.BigIntegerField() #bigintegerfiend that reason becouse there are user write largr data
    number=models.IntegerField()

    def __self__():
        return 
    
    
