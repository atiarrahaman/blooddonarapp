from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField, TimeField 





# Create your models here.

CATEGORY_CHOICES=(
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('O+','O+'),
    ('O-','O-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
) 

Bloodwieght_CHOICES=(
    ('450ml','1 bag'),
    ('900ml','2 bag'),
    ('1350ml','3 bag'),
    ('1800ml','4 bag'),
    ('2250ml','5 bag'),
    ('2700ml','6 bag'),
    
)     
class DonationBlood(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)    
    blood_group= models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    bloodweight= models.CharField(choices=Bloodwieght_CHOICES, max_length=50)
    phone= models.CharField( max_length=50)
    hospital=models.CharField( max_length=50)
    adreess=models.CharField( max_length=50)
    date=models.DateField()
    
    apply_date= models.DateField(auto_now_add=True)
    
    status=models.BooleanField(default=False)
    done_status=models.BooleanField(default=False)
 
    
    def __str__(self):
        return str(self.user)
    
CATEGORY_CHOICES=(
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('O+','O+'),
    ('O-','O-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
) 

Bloodwieght_CHOICES=(
    ('450ml','1 bag'),
    ('900ml','2 bag'),
    ('1350ml','3 bag'),
    ('1800ml','4 bag'),
    ('2250ml','5 bag'),
    ('2700ml','6 bag'),
    
)     
class NeedBlood(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)    
    blood_group= models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    bloodweight= models.CharField(choices=Bloodwieght_CHOICES, max_length=50)
    phone= models.CharField( max_length=50)
    hospital=models.CharField( max_length=50)
    adreess=models.CharField( max_length=50)
    date=models.DateField()
    apply_date= models.DateField(auto_now_add=True)
    status=models.BooleanField(default=False)
    done_status=models.BooleanField(default=False)
    def __str__(self):
        return str(self.user)
    
    
Post_CHOICES=(
    ('blood','blood'),
    ('sports','sports'),
    ('funny','funny'),
    ('adult','adult'),
    ('notice','notice'),
    
    
)  
    
class CreatPost(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    author= models.CharField(max_length=50)
    catagory=models.CharField(choices=Post_CHOICES, max_length=50)
    title= models.CharField(max_length=250)
    text= models.TextField()
    creat_date=models.DateTimeField(auto_now_add=True)
    
    upload_pic = models.ImageField( upload_to='BlogPost')
    check_status= models.BooleanField(default=False)
    approved_status= models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
          ordering= ["-id"]
    


