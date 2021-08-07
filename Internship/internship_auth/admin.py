from django.contrib import admin

# Register your models here.
from Internship.internship_auth.models import InternshipUser

admin.site.register(InternshipUser)