from django.contrib import admin
from .models import Job_Listing, Job_Offer, Job_Application

# Register your models here.
admin.site.register(Job_Listing)
admin.site.register(Job_Offer)
admin.site.register(Job_Application)