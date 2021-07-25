from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from Internship.Choices.choices import FIELD_CHOICES, TYPE_UNKNOWN, CITY_CHOICES, DURATION_CHOICES, EMPLOYMENT_TYPE
from Internship.internship_auth.models import InternshipUser
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile

UserModel = get_user_model()



class Internship_ad(models.Model):
    title = models.CharField(max_length=50)
    city = models.CharField(max_length=30, choices=CITY_CHOICES, default=TYPE_UNKNOWN)
    field = models.CharField(max_length=30, choices=FIELD_CHOICES, default=TYPE_UNKNOWN)
    employment_type = models.CharField(max_length=15, choices=EMPLOYMENT_TYPE, default=TYPE_UNKNOWN)
    duration = models.CharField(max_length=30, choices=DURATION_CHOICES, default=TYPE_UNKNOWN)
    image = models.ImageField()
    description = models.TextField(max_length=500)
    is_active = models.BooleanField(default=True)

    company_owner = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    applied_candidates = models.ManyToManyField(CandidateProfile, blank=True)


# class AppliedData(models.Model):
#     datetime_of_applying = models.DateField(blank=True)
#     applied_candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE)
#     application = models.ForeignKey(Internship_ad, on_delete=models.CASCADE)