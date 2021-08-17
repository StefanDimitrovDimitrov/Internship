from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from Internship.internship_profiles.models import CandidateProfile, CompanyProfile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        if instance.profile == 'Candidate':
            profile = CandidateProfile()
        else:
            profile = CompanyProfile()
        profile.user_id = instance.id
        profile.email = instance.email
        profile.save()


@receiver(pre_save, sender=CandidateProfile)
def check_is_complete(sender, instance, update_fields=None, **kwargs):
    if instance.first_name and instance.last_name and instance.email and instance.profile_image and instance.CV:
        instance.is_complete = True
    else:
        instance.is_complete = False


@receiver(pre_save, sender=CompanyProfile)
def check_is_complete(sender, instance, update_fields=None, **kwargs):
    if instance.company_name and instance.email and instance.company_logo and instance.description and instance.company_phone \
            and instance.company_address and instance.company_website:
        instance.is_complete = True
    else:
        instance.is_complete = False
