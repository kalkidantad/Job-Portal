from django.contrib import admin
from django.urls import path
from job.views import *


urlpatterns = [
    path('contact/', contact, name='contact'),
    path('view_job/<int:job_id>/', view_job, name='view_job'),
    
   
   

]