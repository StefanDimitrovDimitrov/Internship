from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime

from django_summernote.fields import SummernoteTextField

from Internship.choices.choices import FIELD_CHOICES, TYPE_UNKNOWN, CITY_CHOICES, DURATION_CHOICES, EMPLOYMENT_TYPE
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile

UserModel = get_user_model()


class Internship_ad(models.Model):
    created_at = models.DateTimeField(default=datetime.now(), editable=False)
    modified_at = models.DateTimeField(default=datetime.now, editable=False)

    title = models.CharField(max_length=70)
    city = models.CharField(max_length=30, choices=CITY_CHOICES, default=TYPE_UNKNOWN)
    field = models.CharField(max_length=30, choices=FIELD_CHOICES, default=TYPE_UNKNOWN)
    employment_type = models.CharField(max_length=15, choices=EMPLOYMENT_TYPE, default=TYPE_UNKNOWN)
    duration = models.CharField(max_length=30, choices=DURATION_CHOICES, default=TYPE_UNKNOWN)
    description = SummernoteTextField(max_length=30000)
    is_active = models.BooleanField(default=True)

    company_owner = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class AppliedTracking(models.Model):
    applied_at = models.DateTimeField(
        default=datetime.now,
        editable=False
    )
    CV = models.FileField(upload_to='intern_cv', blank=True)

    applied_candidates = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE)
    internship_ads = models.ForeignKey(Internship_ad, on_delete=models.CASCADE)
