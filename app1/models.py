from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TotalDonar(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=50)
    bloodgroup= models.CharField( max_length=50,null=True , blank= True ,) 
    district=models.CharField(max_length=250,null=True , blank= True)
    phone=models.CharField(max_length=50,null=True , blank= True)
    email= models.EmailField(null=True , blank= True)
    last_donate= models.DateField(null=True , blank= True)
    age=models.CharField( max_length=50,null=True , blank= True)
    address= models.CharField( max_length=250 ,null=True , blank= True )
    dob= models.DateField( null=True , blank= True)
    profile_pic=models.ImageField(upload_to='profile_pic',null=True , blank= True)
    def __str__(self):
        return str(self.user)    

