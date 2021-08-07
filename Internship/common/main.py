from Internship.internship_app.models import Internship_ad, AppliedTracking
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile
import os


def get_current_company_from_request(request):
    user_id = request.user.id
    current_company = CompanyProfile.objects.get(user_id=user_id)
    return current_company


def get_current_company(pk):
    current_company = CompanyProfile.objects.get(user_id=pk)
    return current_company


def remove_old_img(img):
    if os.path.exists(img):
        os.remove(img)


def get_current_ad(pk):
    ad = Internship_ad.objects.get(pk=pk)
    return ad


def get_list_of_applied_candidates(pk):
    ad_apply_candidates = AppliedTracking.objects.filter(internship_ads=pk)
    all_candidates = CandidateProfile.objects.all()
    list_of_applied_candidates = [c for c in all_candidates for record in ad_apply_candidates if
                                  c.user_id == record.applied_candidates_id]
    return list_of_applied_candidates


def get_list_active_ads():
    list_all_ads = Internship_ad.objects.all()
    active_ads = [ad for ad in list_all_ads if ad.is_active]
    return active_ads
