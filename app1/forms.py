from django import forms
from django.forms import fields


from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AlldonarSingup(forms.ModelForm):
    class Meta:
        model =TotalDonar
        fields= ['bloodgroup','phone','profile_pic',]
        widgets={
            
            'bloodgroup':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            
            
           
        }
class Singup(UserCreationForm):
    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email','first_name']
        widgets={
            
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
        }
     

        
    # if request.method == 'POST':
    #     fm=Singup(request.POST)
        
    #     if fm.is_valid():
    #         fm.save()
    #         messages.success(request,'Account Created !')
    # else:
    #     fm=Singup()
    # context={
    #     'form':fm
    # }
    
    
            #      {% if messages %}
            #        {% for msz in messages %}
            #          <h3 {% if msz.tags %} class="text-success" {% endif %} >{{msz}}</h3>
            #        {% endfor %}
            #      {% endif %}

            #      {% if form.non_field_errors %}
            #      {% for error in form.non_field_errors %}
            #        <p class="text-danger">{{error}}</p>
            #      {% endfor %}
            #    {% endif %}
            #    {{form.none_field_errors}}