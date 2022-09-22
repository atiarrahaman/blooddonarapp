from django.urls import path
from . import views
urlpatterns = [
   
    path('',views.BlogPost , name= 'blogpost'),
    path('postdetails/<int:id>',views.DetailsBlog , name= 'detailsBlogpost'),
    
    path('camping',views.Capming , name= 'camping'),
    path('singup',views.SingUp , name= 'singup'),
    
    path('login',views.Login , name= 'login'),
    path('logout',views.Logout , name= 'logout'),
    path('viewprofile',views.ProfileView , name= 'viewprofile'),
]
