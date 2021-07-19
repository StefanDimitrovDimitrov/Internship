
from django.db import models

# Create your models here.
from Internship.Choices.choices import FIELD_CHOICES, TYPE_UNKNOWN, CITY_CHOICES, DURATION_CHOICES

class Internship_ad(models.Model):
    title = models.CharField(max_length=50)
    city = models.CharField(max_length=30, choices=CITY_CHOICES, default=TYPE_UNKNOWN)
    field = models.CharField(max_length=30, choices=FIELD_CHOICES, default=TYPE_UNKNOWN)
    duration = models.CharField(max_length=30, choices=DURATION_CHOICES, default=TYPE_UNKNOWN)
    image = models.ImageField()
    description = models.TextField(max_length=500)

    # company_profile = models.ForeignKey(Profile, on_delete=models.CASCADE,default='')
    def __str__(self):
        return f'{self.id};{self.title};{self.city};{self.field};{self.duration};'
