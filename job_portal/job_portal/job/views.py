from django.shortcuts import render, HttpResponse ,redirect
from .models import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, LoginForm 
from django.contrib.auth import authenticate, login
from django.db.models import Count

# Create your views here.
from django.shortcuts import render
from .models import Job



def home(request):
    company_info = CompanyInformation.objects.first()  
    if company_info is None:
        company_info = CompanyInformation()  

    if request.method == 'POST':
        title = request.POST.get('title', '').lower()
        location = request.POST.get('location', '').lower()
        jobs = Job.objects.filter(title__icontains=title, location__icontains=location)
    else:
        jobs = Job.objects.all()  # for a GET request

    job_counts = Job.objects.values('category__name').annotate(total=Count('category')).order_by('category__name')

    context = {
        'company_info': company_info,
        'filteredJobs': jobs,  # pass the Job model instances directly
        'jobCounts': job_counts,
        'is_post_request': request.method == 'POST'
    }

    return render(request, 'home.html', context)




def about(request):
    company_info = CompanyInformation.objects.first()  # get the first CompanyInformation instance
    if company_info is None:
        company_info = CompanyInformation()  # create a default instance if none exists
    context = {'company_info': company_info}
    return render(request, 'about.html', context)

def contact(request):
    company_info = CompanyInformation.objects.first()  
    if company_info is None:
        company_info = CompanyInformation()  
    context = {'company_info': company_info}


    if request.method=="POST":
        contact=Contactus()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message = request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.message=message
        contact.save()
    
    return render(request, 'contact.html',context)
def job_list(request):
    company_info = CompanyInformation.objects.first()  
    if company_info is None:
        company_info = CompanyInformation()  

    if request.method == 'POST':
        title = request.POST.get('title', '').lower()
        location = request.POST.get('location', '').lower()
        salary = request.POST.get('salary', '').lower()
        job_type = request.POST.get('job_type', '').lower()

        jobs = Job.objects.filter(
            title__icontains=title,
            location__icontains=location,
            salary__icontains=salary,
            job_type__icontains=job_type
        )
    else:
        jobs = Job.objects.all()  # for a GET request

    context = {
        'company_info': company_info,
        'filteredJobs': jobs,  # pass the Job model instances directly
        'is_post_request': request.method == 'POST'
    }

    return render(request, 'jobs.html', context)


def register(request):
    company_info = CompanyInformation.objects.first()  
    if company_info is None:
        company_info = CompanyInformation()  

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            loggedInUser.objects.create(name=user.username, email=user.email)   
            return redirect('job') 
    else:
        form = RegistrationForm()

    context = {'company_info': company_info, 'form': form}
    
    return render(request, 'register.html', context)


def custom_login(request):
    company_info = CompanyInformation.objects.first()  # get the first CompanyInformation instance
    if company_info is None:
        company_info = CompanyInformation()  # create a default instance if none exists

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)  
                return redirect('jobs')
            else:
                form.add_error(None, "Invalid login credentials. Please try again.")
    else:
        form = LoginForm()

    context = {
        'company_info': company_info,
        'form': form
    }

    return render(request, 'login.html', context)


def view_job(request, job_id):
    company_info = CompanyInformation.objects.first()  
    if company_info is None:
        company_info = CompanyInformation()  

    job = Job.objects.get(pk=job_id)

    context = {
        'company_info': company_info,
        'job': job
    }

    return render(request, 'view_job.html', context)



