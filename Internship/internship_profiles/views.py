from django.shortcuts import render


# Create your views here.
from Internship.internship_profiles.forms import CompanyForm


def get_company_profile(request):
    # profile = CompanyForm.object.all()
    #
    # context = {
    #     'profile': profile
    # }
    #
    # return render(request, 'profile/company.html', context)
    pass

def edit_company_profile(request):
    pass


def delete_company_profile(request):
    pass


def get_candidate_details(request):
    pass


def edit_candidate_details(request):
    pass


def delete_candidate_details(request):
    pass
