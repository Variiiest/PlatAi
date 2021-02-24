from django.db import models
# Create your models here.
from django.conf import	settings
class Profile(models.Model):
    STATUS_CHOICES= (
        ('Open to work', 'Open to work'),
        ('Working', 'Working'),
    )
    user=	models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='profile')	
    profession= models.CharField(max_length=100, blank=True, null=True)
    resume_link= models.URLField(max_length= 100, blank=True, null=True)
    file = models.ImageField(upload_to='users/%Y/%m/%d/', blank= True,default='create.jpg')
    status= models.CharField(max_length=30, choices= STATUS_CHOICES, default= 'Working')
    bio = models.TextField(blank=True, null=True)
    phone= models.CharField(max_length=10,blank=True, null=True)
   

    def __str__(self):
        return 'Profile for User {}'.format(self.user)
