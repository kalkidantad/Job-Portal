from django.contrib import admin

from .models import * #for managing info to implement dynamic

# Register your models here.
admin.site.register(CompanyInformation)
admin.site.register(loggedInUser)
admin.site.register(Category)
admin.site.register(CompanyProfile)
admin.site.register(Job)
admin.site.register(Bookmark)
admin.site.register(Contactus)
