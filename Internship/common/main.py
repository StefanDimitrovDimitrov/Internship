from Internship.internship_profiles.models import CompanyProfile
import os


def get_current_company(request):
    user = request.user
    current_company = CompanyProfile.objects.get(user_id=user.id)
    return current_company


def remove_old_img(img):
    if os.path.exists(img):
        os.remove(img)
