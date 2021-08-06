from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Internship.common.main import get_current_company
from Internship.internship_profiles.signals import *
# Create your views here.
from Internship.internship_app.models import Internship_ad, AppliedTracking

from Internship.internship_profiles.forms import EditCompanyForm, EditCandidateForm
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile

UserModel = get_user_model()


def get_company_profile(request, pk):
    company = get_current_company(pk)
    company_ads = Internship_ad.objects.filter(company_owner=pk)
    records = AppliedTracking.objects.filter()

    for ad in company_ads:
        num_candidates = records.filter(application_id=ad.id).count()
        ad.num_candidates = num_candidates

    context = {
        'info': company,
        'company_ads': company_ads
    }

    return render(request, 'profile/company_profile.html', context)


@login_required
def edit_company_profile(request, pk):
    company = CompanyProfile.objects.get(pk=pk)

    if request.method == "POST":
        edit_profile_form = EditCompanyForm(request.POST, request.FILES, instance=company)
        if edit_profile_form.is_valid():
            edit_profile_form.save()
            return redirect('company profile', pk=pk)
        else:
            context = {
                'form': EditCompanyForm(instance=company),
                'info': company,
                'errors': edit_profile_form.errors
            }
            return render(request, 'profile/edit_company_profile.html', context)

    context = {
        'form': EditCompanyForm(instance=company),
        'info': company,
    }

    return render(request, 'profile/edit_company_profile.html', context)


@login_required
def get_candidate_profile(request, pk):
    candidate = CandidateProfile.objects.get(pk=pk)
    candidate_ads = AppliedTracking.objects.filter(applied_candidate_id=pk)
    all_ads = Internship_ad.objects.all()
    list_of_ads = [ad for ad in all_ads for candidate_ad in candidate_ads if ad.id == candidate_ad.application_id]
    print(list_of_ads)

    context = {
        'info': candidate,
        'list_of_ads': list_of_ads
    }

    return render(request, 'profile/candidate_profile.html', context)


@login_required
def edit_candidate_profiles(request, pk):
    candidate = CandidateProfile.objects.get(pk=pk)

    if request.method == "POST":

        profile_form = EditCandidateForm(request.POST, request.FILES, instance=candidate)

        if profile_form.is_valid():
            profile_form.save()
            return redirect('candidate profile', pk=pk)

    context = {
        'profile_form': EditCandidateForm(instance=candidate),
        'info': candidate,
    }

    return render(request, 'profile/edit_candidate_profile.html', context)


@login_required
def delete_user(request, pk):
    user = UserModel.objects.get(pk=pk)
    user.delete()
    return redirect('home')
