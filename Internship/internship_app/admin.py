from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

from Internship.internship_app.models import Internship_ad
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('description', )





admin.site.register(Internship_ad, SomeModelAdmin)