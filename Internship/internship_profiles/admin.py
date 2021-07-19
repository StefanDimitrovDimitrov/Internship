from django.contrib import admin

# Register your models here.
from Internship.internship_profiles.models import CandidateProfile, CompanyProfile

admin.site.register(CandidateProfile)
admin.site.register(CompanyProfile)