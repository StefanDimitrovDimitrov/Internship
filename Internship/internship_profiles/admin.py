from django.contrib import admin

# Register your models here.
from Internship.internship_profiles.models import CandidateProfile, CompanyProfile

class IntenShipAdmin(admin.ModelAdmin):
    list_display=['title','city','field','employment_type',]
    sorted_by=['is_active']
    list_filter=['is_active']


admin.site.register(CandidateProfile)
admin.site.register(CompanyProfile)