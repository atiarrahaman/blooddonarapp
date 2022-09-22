from django.contrib import admin
from .models import *


from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Register your models here.


    

admin.site.register(DonationBlood)
admin.site.register(NeedBlood)
admin.site.register(CreatPost)
