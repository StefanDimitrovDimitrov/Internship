from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from Internship.Choices.choices import FIELD_CHOICES, TYPE_UNKNOWN, CITY_CHOICES, DURATION_CHOICES
from Internship.internship_auth.models import InternshipUser
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile

UserModel = get_user_model()



class Internship_ad(models.Model):
    title = models.CharField(max_length=50)
    city = models.CharField(max_length=30, choices=CITY_CHOICES, default=TYPE_UNKNOWN)
    field = models.CharField(max_length=30, choices=FIELD_CHOICES, default=TYPE_UNKNOWN)
    duration = models.CharField(max_length=30, choices=DURATION_CHOICES, default=TYPE_UNKNOWN)
    image = models.ImageField()
    description = models.TextField(max_length=500)

    company_owner = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    applied_candidates = models.ManyToManyField(CandidateProfile, blank=True)

    # user = models.ForeignKey(
    #     UserModel,
    #     on_delete=models.CASCADE,
    # )

    # company_profile = models.ForeignKey(Profile, on_delete=models.CASCADE,default='')
    def __str__(self):
        return f'{self.id};{self.title};{self.city};{self.field};{self.duration};'
