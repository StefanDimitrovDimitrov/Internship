from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Internship.common.main import get_current_company, get_current_ad, get_list_of_applied_candidates
from Internship.internship_profiles.signals import *
# Create your views here.
from Internship.internship_app.models import Internship_ad, AppliedTracking

from Internship.internship_profiles.forms import EditCompanyForm, EditCandidateForm
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile

UserModel = get_user_model()


def get_company_profile(request, pk):
    company = get_current_company(pk)
    company_ads_active = Internship_ad.objects.filter(company_owner=pk).filter(is_active=True)
    company_ads_closed = Internship_ad.objects.filter(company_owner=pk).filter(is_active=False)

    records = AppliedTracking.objects.filter()

    for ad in company_ads_active:
        num_candidates = records.filter(internship_ads=ad.id).count()
        ad.num_candidates = num_candidates

    for ad in company_ads_closed:
        num_candidates = records.filter(internship_ads=ad.id).count()
        ad.num_candidates = num_candidates

    context = {
        'info': company,
        'company_ads_active': company_ads_active,
        'company_ads_closed': company_ads_closed
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
    candidate_ads = AppliedTracking.objects.filter(applied_candidates_id=pk).distinct('internship_ads_id')
    list_of_ads = reversed(candidate_ads)
    context = {
        'info': candidate,
        'list_of_ads': list_of_ads,
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


@login_required
def applied_candidates(request, pk):
    ad = get_current_ad(pk)
    ad_apply_candidates = AppliedTracking.objects.filter(internship_ads=pk)


    # list_of_applied_candidates = get_list_of_applied_candidates(pk)
    num_candidates = len(ad_apply_candidates)

    context = {
        # 'candidates': list_of_applied_candidates,
        'ad': ad,
        'records': ad_apply_candidates,
        'num_candidates': num_candidates
    }

    return render(request, 'internship/applied_candidates.html', context)
