from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from Internship.internship_profiles.models import CandidateProfile, CompanyProfile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        if instance.profile == 'Candidate':
            profile = CandidateProfile(user=instance,)
            profile.email = instance.email
        else:
            profile = CompanyProfile(user=instance,)
            profile.company_name = instance.company_name
            profile.email = instance.email


        profile.save()