from Internship.internship_app.models import Internship_ad, AppliedTracking
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile
import os


def get_current_company(request):
    user = request.user
    current_company = CompanyProfile.objects.get(user_id=user.id)
    return current_company


def remove_old_img(img):
    if os.path.exists(img):
        os.remove(img)

def get_current_ad(pk):
    ad = Internship_ad.objects.get(pk=pk)
    return ad

def get_list_of_applied_candidates(pk):
    ad_apply_candidates = AppliedTracking.objects.filter(application_id=pk)
    all_candidates = CandidateProfile.objects.all()
    list_of_applied_candidates = [c for c in all_candidates for record in ad_apply_candidates if
                                  c.user_id == record.applied_candidate_id]
    return list_of_applied_candidates