from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.shortcuts import render, redirect

from Internship.common.main import get_current_company, get_current_ad
from Internship.internship_app.models import Internship_ad, AppliedTracking
from Internship.internship_profiles.signals import *
# Create your test_views here.


from Internship.internship_profiles.forms import EditCompanyForm, EditCandidateForm
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile

UserModel = get_user_model()


def get_company_profile(request, pk):

    try:
        company = get_current_company(pk)
    except ObjectDoesNotExist:
        return redirect('home')

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
    form = EditCompanyForm(instance=company)

    if request.method == "POST":
        form = EditCompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            current_company_info = form.save(commit=False)

            if current_company_info != '':
                all_companies = CompanyProfile.objects.all()
                for companies in all_companies:
                    if companies.user_id != pk:
                        if companies.company_name == current_company_info.company_name:
                            context = {
                                'form': EditCompanyForm(instance=company),
                                'info': company,
                                'errors': ValidationError('A company with this name already exists')
                            }
                            return render(request, 'profile/edit_company_profile.html', context)



            request.user.email = current_company_info.email
            request.user.save()
            current_company_info.save()
            return redirect('company profile', pk=pk)
    context = {
        'form': form,
        'info': company,
    }

    return render(request, 'profile/edit_company_profile.html', context)


@login_required
def get_candidate_profile(request, pk):

    try:
        candidate = CandidateProfile.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return redirect('home')


    records = AppliedTracking.objects.filter(internship_ads__is_active=True).filter(applied_candidates_id=pk).order_by(
        'applied_at')

    list_of_ads = records

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
            temp_info = profile_form.save(commit=False)
            request.user.email = temp_info.email
            request.user.save()
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
    ad_apply_candidates = AppliedTracking.objects.filter(internship_ads=pk).order_by('-applied_at')
    num_candidates = len(ad_apply_candidates)
    count = 0
    context = {
        'count': count,
        'ad': ad,
        'records': ad_apply_candidates,
        'num_candidates': num_candidates
    }

    return render(request, 'internship/applied_candidates.html', context)
