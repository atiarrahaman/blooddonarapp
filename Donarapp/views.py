from django.shortcuts import redirect, render
from .models import *
from .forms import *
from app1.models import TotalDonar
from django.contrib import messages
# Create your views here.
def Dashbord(request):
    if request.user.is_authenticated:
       if request.user.is_superuser == True:
           return redirect ('/admindashboard')  
       return render (request,'dashboad.html')
    else:
        return redirect('/login')
def Profile(request):
    if request.user.is_authenticated:
      data=TotalDonar.objects.get(user=request.user)
      bloodgrp_alluser=TotalDonar.objects.filter()
      context={
          'data':data
      }
      return render (request,'profile.html',context)
    else:
        return redirect('/login')
def ProfileEdit(request):
  if request.user.is_authenticated:    
    
    if request.method == 'POST':
      ed=TotalDonar.objects.get(user=request.user )
      fm=Profile_Edit_Form(request.POST,request.FILES  , instance=ed )
      if fm.is_valid():
            fm.save()
         
            return redirect('/profile')
    else:
        ed=TotalDonar.objects.get(user=request.user)
        fm=Profile_Edit_Form(instance=ed)
    return render(request,'profileedit.html',{'form':fm})
  else:
        return redirect('/login')
def DonarCreat(request):
    if request.user.is_authenticated:
    
        if request.method =='POST':
           fm=Profile_Edit_Form(request.POST ,request.FILES) 
           if fm.is_valid():
               fm = fm.save(commit=False)
               fm.user=request.user
               fm=fm.save()
               return redirect('/profile')
        else:
            fm=Profile_Edit_Form() 
            
        context={
            'form':fm
        }
        return render (request,'donarcreate.html',context)
   
    else:
        return redirect('/login')
def Donation_Blood(request):
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            fm= ApplyBloodForm(request.POST)
            if fm.is_valid():
                fm = fm.save(commit=False)
                fm.user=request.user
                fm=fm.save()
                messages.success(request,'Apllication Submit Successfull !!')
                fm=ApplyBloodForm() 
        else:
            fm=ApplyBloodForm() 
    
        context={'form':fm}
        return render (request,'applyblood.html',context)
    else:
        return redirect('/login')
def Donation_History(request):
    if request.user.is_authenticated:
        donation_history=DonationBlood.objects.filter(user=request.user)
        context={
            'donation_history':donation_history
        }  
        return render (request ,'donation-history.html',context) 
    else:
        return redirect('/login') 
def ApplyNeedBlood(request):
    
    if request.user.is_authenticated:
            
        if request.method == 'POST':
            fm= ApplyNeddBloodForm(request.POST)
            if fm.is_valid():
                fm = fm.save(commit=False)
                fm.user=request.user
                fm=fm.save()
                messages.success(request,'Apllication Submit Successfull !!')
                fm=ApplyNeddBloodForm() 
        else:
            fm=ApplyNeddBloodForm() 
    
        context={'forms':fm}
        return render(request,'needbloodform.html',context)
    else:
        return redirect('/login')


def NeddBloodHistorys(request):
  if request.user.is_authenticated:
    fm=NeedBlood.objects.filter(user=request.user)
    
    context={'fm':fm}
    return render (request,'needbloodhistory.html',context)
  else:
      return redirect('/login')
def BlogPost(request):
    if request.user.is_authenticated:
    
        if request.method == 'POST':
            fm= CreatePostForm(request.POST ,request.FILES )
            if fm.is_valid():
                fm = fm.save(commit=False)
                fm.user=request.user
                fm=fm.save()
                messages.success(request,'Create  Post successfull !!')
                fm=CreatePostForm() 
        else:
            fm=CreatePostForm() 
    
        context={'forms':fm}
        return render(request,'post-form.html',context)   
    else:
        return redirect('/login')
        


