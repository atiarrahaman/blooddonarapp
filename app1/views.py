from multiprocessing import context
from django.shortcuts import redirect, render
from Donarapp.models import DonationBlood 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout 
from django.contrib import messages
from .forms  import *
from Donarapp.models import CreatPost
from .models import TotalDonar

# Create your views here.
def SingUp(request):
    if request.method == 'POST':
        fm=Singup(data=request.POST)
        form=AlldonarSingup(data=request.POST)
        if fm.is_valid() and form.is_valid():
           user= fm.save()
           user.set_password(user.password)
           
           user_form=form.save(commit=False)
           user_form.user=user
           if 'profile_pic' in request.FILES:
               user_form.profile_pic = request.FILES['profile_pic']
           user_form.save()   
           messages.success(request,'Account Created !')
    else:
        fm=Singup()
        form=AlldonarSingup()
  
    context={'fm':fm, 'form':form}
   
    return render(request,'singup.html',context)



def Login(request):
    if  request.method == 'POST':
        fm =AuthenticationForm(request=request, data= request.POST) 
        if fm.is_valid():
            messages.success(request,'Login Successfull !!')
            uname=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            user=authenticate(username=uname,password=password)
            if user is not None:
                login(request ,user)
                return redirect('/dashboard')
            
            
                    
                    
    else:
        fm =AuthenticationForm() 
   
    context={'login':'active','form':fm}
    return render (request,'login.html',context)
def Logout(request):
        logout(request)
        messages.success(request,'Logout Successfull !!')
        return redirect('/login')   



def BlogPost(request):
    post=CreatPost.objects.all()
   
    
    context={'blogpost':'active' ,'post':post}
    return render (request,'blogpost.html',context)
def DetailsBlog(request,id):
    dpost=CreatPost.objects.get(id=id)
    context={
        'post':dpost,
    }
    return render(request,'blogPostDetails.html',context)
def Capming(request):

    context={'camping':'active'}
    return render (request,'camping.html',context)

def ProfileView(request):
    data=TotalDonar.objects.filter(id=12)
    context={'data':data}
    return render (request,"profileview.html",context)