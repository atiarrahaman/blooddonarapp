from django.urls import path 
from . import views

urlpatterns = [
    path('admindashboard',views.Home , name='admin_dashboard'),
    path('giveblood',views.Giveblood , name='give_blood'),
    path('needblood',views.Needblood , name='need_blood'),
    path('alldonars',views.AllDonars , name='all-donars'),
    path('donation-status',views.DonateBloodAdmin , name='donation-status'),
    path('movedonar/<int:id>/<int:sts>',views.Move , name='movedonar'),
    path('rejects/<int:id>/<int:sts>',views.Rejects , name='rejects'),
    path('request-status',views.RequstBlood , name='request_status'),
    path('moverequest/<int:id>/<int:sts>',views.MoveRequstBlood , name='move_request_status'),
    path('rejectsrequest/<int:id>/<int:sts>',views.RejectsRequest , name='rejectsrequest'),
    path('bloog-post',views.BloogPOstStatus , name='bloog_post'),
    path('test',views.Test , name='test'),
    
]




















