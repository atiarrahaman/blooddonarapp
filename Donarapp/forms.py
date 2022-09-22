from tkinter import Widget
from django import forms
from django.forms import fields
from .models import *
from app1.models import TotalDonar
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

      
class ApplyBloodForm(forms.ModelForm):
    class Meta:
        model=DonationBlood
        fields='__all__'
        exclude=['user','apply_date','status','done_status']
        widgets={
            
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'hospital':forms.TextInput(attrs={'class':'form-control'}),
            'adreess':forms.TextInput(attrs={'class':'form-control'}),
            'date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
        }
class ApplyNeddBloodForm(forms.ModelForm):
    class Meta:
        model=NeedBlood
        fields='__all__'
        exclude=['user','apply_date','status','done_status']
        widgets={
            
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'hospital':forms.TextInput(attrs={'class':'form-control'}),
            'adreess':forms.TextInput(attrs={'class':'form-control'}),
            'date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
        }        
        
class Profile_Edit_Form(forms.ModelForm):
    
    class Meta:
        model=TotalDonar
        fields='__all__'
        exclude=['user','name']
        widgets={
            
            'bloodgroup':forms.TextInput(attrs={'class':'form-control'}),
            'district':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'last_donate':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','type':'date'}),
           
        }
        
class CreatePostForm(forms.ModelForm):
    class Meta:
        model=CreatPost
        fields= ['author','catagory','title','text','upload_pic']
        
        widgets={
            
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'text':forms.Textarea(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control' , 'value':'','id':'next','type':'hidden'}),
            'catagory':forms.Select(attrs={'class':'form-control'}),
            
           
        } 

        