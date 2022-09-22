

from django.urls import path 
from . import views


urlpatterns = [
    
   
   path('dashboard',views.Dashbord, name='dashboard'),
   path('profile',views.Profile, name='profile'),
   path('donation-blood',views.Donation_Blood, name='donation_blood'),
   path('donation-history',views.Donation_History, name='donation_history'),
   path('apply-need-blood',views.ApplyNeedBlood, name='apply_need_blood'),
   path('need-blood-history',views.NeddBloodHistorys, name='need_blood_history'),
   
   path('profile-edit',views.ProfileEdit, name='profile_edit'),
   path('donar-creat',views.DonarCreat, name='donar_creat'),
   path('creat-post',views.BlogPost, name='creat_post'),
   
   
    
    
]
