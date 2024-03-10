from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# class Information of the Company 

class CompanyInformation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    why_choose_us = models.TextField()
    image = models.ImageField(upload_to='company_images/')
    location = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20)


    def __str__(self):
        return self.name


class loggedInUser(models.Model):
    name= models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    

    def __str__(self):
        return self.email
    
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
  

#     def __str__(self):
#         return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 


class CompanyProfile(models.Model):
    company_name = models.CharField(max_length=100)
    website_url = models.URLField(blank=True, null=True) 

    def __str__(self):
        return self.company_name

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    qualifications = models.TextField()
    job_type = models.CharField(max_length=50)
    published_date = models.DateTimeField(auto_now_add=True,blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Bookmark(models.Model):
    loggedin = models.ForeignKey(loggedInUser, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.loggedin.email}'s bookmark for {self.job.title}"


class Contactus(models.Model):
    name= models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    message=models.TextField()
    def __str__(self) -> str:
        return self.name