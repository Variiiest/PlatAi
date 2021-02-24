from django.db import models

# Create your models here.
class ContactBusiness(models.Model):
    name= models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    message= models.TextField(max_length=1000)
    
    objects= models.Manager()  
    def __str__(self):
        return self.email