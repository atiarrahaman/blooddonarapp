from django.shortcuts import redirect, render
from app1.models import TotalDonar 

from Donarapp.models import DonationBlood ,NeedBlood ,CreatPost
from django.contrib.auth.models import User

from django.db.models import Q
# Create your views here.
def Home(request):
   if request.user.is_superuser: 
        alldonar= TotalDonar.objects.all().count()
        a= TotalDonar.objects.filter(bloodgroup= 'a+' ) .all().count()
        A= TotalDonar.objects.filter(bloodgroup= 'A+' ).all().count()
        
        b= TotalDonar.objects.filter(bloodgroup= 'b+' ) .all().count()
        B= TotalDonar.objects.filter(bloodgroup= 'B+' ).all().count()
        
        o= TotalDonar.objects.filter(bloodgroup= 'o+' ) .all().count()
        O= TotalDonar.objects.filter(bloodgroup= 'O+' ).all().count()
        
        ab= TotalDonar.objects.filter(bloodgroup= 'ab+' ) .all().count()
        AB= TotalDonar.objects.filter(bloodgroup= 'AB+' ).all().count()
        Ab= TotalDonar.objects.filter(bloodgroup= 'Ab+' ).all().count()
        
        an= TotalDonar.objects.filter(bloodgroup= 'a-' ) .all().count()
        An= TotalDonar.objects.filter(bloodgroup= 'A-' ).all().count()
        
        bn= TotalDonar.objects.filter(bloodgroup= 'b-' ) .all().count()
        Bn= TotalDonar.objects.filter(bloodgroup= 'B-' ).all().count()
        
        on= TotalDonar.objects.filter(bloodgroup= 'o-' ) .all().count()
        On= TotalDonar.objects.filter(bloodgroup= 'O-' ).all().count()
        
        
        abn= TotalDonar.objects.filter(bloodgroup= 'ab-' ) .all().count()
        ABn= TotalDonar.objects.filter(bloodgroup= 'AB-' ).all().count()
        Abn= TotalDonar.objects.filter(bloodgroup= 'Ab-' ).all().count()
        
        
        context={'alldonar':alldonar ,'b':b+B ,
                'a':a+A ,'o':o+O ,'ab':ab+AB+Ab,
                "an":an+An,'bn':bn+Bn,'on':on+On,'abn':abn+ABn+Abn}
        
        return render(request,'admin-dashboad.html',context)
   else:
       return redirect('login')

def Giveblood(request):
    if request.user.is_superuser: 
        total= DonationBlood.objects.filter(done_status=False ,status= False).count()
        a= DonationBlood.objects.filter(status= False,done_status=False, blood_group= 'a+', ) .all().count()
        A= DonationBlood.objects.filter(status= False,done_status=False,blood_group= 'A+' ).all().count()
        
        b= DonationBlood.objects.filter(status= False,done_status=False,blood_group= 'b+' ) .all().count()
        B= DonationBlood.objects.filter(status= False,done_status=False,blood_group= 'B+' ).all().count()
        
        o= DonationBlood.objects.filter(status= False,done_status=False,blood_group= 'o+' ) .all().count()
        O= DonationBlood.objects.filter(status= False,done_status=False,blood_group= 'O+' ).all().count()
        
        ab= DonationBlood.objects.filter(status= False,done_status=False,blood_group= 'ab+' ) .all().count()
        AB= DonationBlood.objects.filter(status= False,done_status=False,blood_group= 'AB+' ).all().count()
        Ab= DonationBlood.objects.filter(status= False,done_status=False,blood_group= 'Ab+' ).all().count()
        
        an= DonationBlood.objects.filter(status= False,done_status=False,blood_group= 'a-' ) .all().count()
        An= DonationBlood.objects.filter(status= False,done_status=False,blood_group= 'A-' ).all().count()
        
        bn= DonationBlood.objects.filter(status= False,done_status=False,blood_group= 'b-' ) .all().count()
        Bn= DonationBlood.objects.filter(status= False,done_status=False,blood_group= 'B-' ).all().count()
        
        on= DonationBlood.objects.filter(status= False,done_status=False,blood_group= 'o-' ) .all().count()
        On= DonationBlood.objects.filter(status= False,done_status=False,blood_group= 'O-' ).all().count()
        
        
        abn= DonationBlood.objects.filter(status= False,done_status=False,blood_group= 'ab-' ) .all().count()
        ABn= DonationBlood.objects.filter(status= False,done_status=False,blood_group= 'AB-' ).all().count()
        Abn= DonationBlood.objects.filter(status= False,done_status=False,blood_group= 'Ab-' ).all().count()
        
        
        context={'total':total ,'b':b+B ,
                'a':a+A ,'o':o+O ,'ab':ab+AB+Ab,
                "an":an+An,'bn':bn+Bn,'on':on+On,'abn':abn+ABn+Abn}
        return render ( request,'bloodgive.html',context)
    else:
           return redirect('login')

def Needblood(request):
    if request.user.is_superuser:
            
        total= NeedBlood.objects.filter(done_status=False ,status= False).count()
        a= NeedBlood.objects.filter(status= False,done_status=False, blood_group= 'a+', ) .all().count()
        A= NeedBlood.objects.filter(status= False,done_status=False,blood_group= 'A+' ).all().count()
        
        b= NeedBlood.objects.filter(status= False,done_status=False,blood_group= 'b+' ) .all().count()
        B= NeedBlood.objects.filter(status= False,done_status=False,blood_group= 'B+' ).all().count()
        
        o= NeedBlood.objects.filter(status= False,done_status=False,blood_group= 'o+' ) .all().count()
        O= NeedBlood.objects.filter(status= False,done_status=False,blood_group= 'O+' ).all().count()
        
        ab= NeedBlood.objects.filter(status= False,done_status=False,blood_group= 'ab+' ) .all().count()
        AB= NeedBlood.objects.filter(status= False,done_status=False,blood_group= 'AB+' ).all().count()
        Ab= NeedBlood.objects.filter(status= False,done_status=False,blood_group= 'Ab+' ).all().count()
        
        an= NeedBlood.objects.filter(status= False,done_status=False,blood_group= 'a-' ) .all().count()
        An= NeedBlood.objects.filter(status= False,done_status=False,blood_group= 'A-' ).all().count()
        
        bn= NeedBlood.objects.filter(status= False,done_status=False,blood_group= 'b-' ) .all().count()
        Bn= NeedBlood.objects.filter(status= False,done_status=False,blood_group= 'B-' ).all().count()
        
        on= NeedBlood.objects.filter(status= False,done_status=False,blood_group= 'o-' ) .all().count()
        On= NeedBlood.objects.filter(status= False,done_status=False,blood_group= 'O-' ).all().count()
        
        
        abn= NeedBlood.objects.filter(status= False,done_status=False,blood_group= 'ab-' ) .all().count()
        ABn= NeedBlood.objects.filter(status= False,done_status=False,blood_group= 'AB-' ).all().count()
        Abn= NeedBlood.objects.filter(status= False,done_status=False,blood_group= 'Ab-' ).all().count()
        
        
        context={'total':total ,'b':b+B ,
                'a':a+A ,'o':o+O ,'ab':ab+AB+Ab,
                "an":an+An,'bn':bn+Bn,'on':on+On,'abn':abn+ABn+Abn}
        return render ( request,'bloodneed.html',context)
    else:
           return redirect('login')
def AllDonars(request):
    if request.user.is_superuser:
        if 'q' in request.GET:
            q=request.GET['q']
            multiple_q= Q(Q(user__username__iexact=q)|Q (bloodgroup__iexact=q)|Q (district__iexact=q)|Q (phone__iexact=q)|Q (email__iexact=q)|Q (age__iexact=q))
            alldonar=TotalDonar.objects.filter(multiple_q)
        else:
            alldonar=TotalDonar.objects.all()
        context={'alldonar':alldonar}
        
        return render (request,'adminalldonarlist.html',context)
    else:
           return redirect('login')
def DonateBloodAdmin(request):
    if request.user.is_superuser:
        fm=DonationBlood.objects.filter(status = False)
        
        context={'table':fm}
        return render(request,'donatebloodadmin.html',context)
    else:
           return redirect('login')
def Move(request ,id ,sts):
    donar=DonationBlood.objects.get(id=id)
    donar.status = True
    if sts== 1 :
        donar.done_status = True
        donar=donar.save()
    else:
        donar.done_status = False
        donar=donar.save()
        
    
    return redirect('/donation-status')

def Rejects(request,id ,sts):
    donar=DonationBlood.objects.get(id=id)
    donar.status = True
    if sts== 0 :
        donar.done_status = False
        donar=donar.save()
    
    return redirect('/donation-status')
def RequstBlood(request):
    if request.user.is_superuser:
        request_list=NeedBlood.objects.filter(status= False)
        context={'request_list':request_list}
        return render(request,'requestblood.html',context)
    else:
           return redirect('login')

def MoveRequstBlood(request,id,sts):
    request=NeedBlood.objects.get(id=id)
    request.status = True
    if sts== 1 :
        request.done_status = True
        request=request.save()
    else:
        request.done_status = False
        request=request.save()
        
    return redirect('/request-status')

def RejectsRequest(request ,id,sts):
    rejects_request=NeedBlood.objects.get(id=id)
    rejects_request.status= True
    if sts == 0:
        rejects_request.done_status= False
        rejects_request=rejects_request.save()
        
    return redirect('/request-status')

def BloogPOstStatus(request):
    # blogpost=CreatPost.objects.filter(check_status= False)
    # context={'blogpost':blogpost}
    return render(request,'blogpostlist.html')
def Test(request):
    
    return render(request,'index.html')
