from Internship.internship_profiles.models import CompanyProfile


def get_current_company(request):
    user = request.user
    current_company = CompanyProfile.objects.get(user_id=user.id)
    return current_company