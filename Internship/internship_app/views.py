import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from Internship.common.main import get_current_company, get_current_ad, get_list_of_applied_candidates
from Internship.common.main import remove_old_img
from Internship.internship_app.forms import AdForm, ApplyForm
from Internship.internship_app.models import Internship_ad, AppliedTracking
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile
from django.contrib import messages


class Home(ListView):
    model = Internship_ad
    template_name = 'shared/base.html'
    context_object_name = 'ads'
    paginate_by = 3


def catalog_companies(request):
    companies = CompanyProfile.objects.filter(is_complete=True)

    context = {
        'companies': companies
    }

    return render(request, 'internship/catalog_companies.html', context)


def catalog_ad(request):
    list_all_ads = Internship_ad.objects.all()

    ads = [ad for ad in list_all_ads if ad.is_active]

    context = {
        'ads': ads
    }

    return render(request, 'internship/catalog_ads.html', context)


@login_required
def create_ad(request):
    current_company = get_current_company(request)
    form = AdForm()
    if request.method == "POST":

        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.company_owner_id = current_company.user_id
            ad.save()
            form.save()
            return redirect('catalog ads')

    context = {
        'form': form,
        'company_profile': current_company

    }
    return render(request, 'internship/create_ad.html', context)


def details_ad(request, pk):
    ad = get_current_ad(pk)
    list_of_applied_candidates = get_list_of_applied_candidates(pk)
    num_candidates = len(list_of_applied_candidates)
    context = {
        'ad': ad,
        'candidates': list_of_applied_candidates,
        'num_candidates': num_candidates
    }

    return render(request, 'internship/details_ad.html', context)


@login_required
def edit_ad(request, pk):
    ad = get_current_ad(pk)
    old_image = ''
    if request.method == "POST":
        if ad.image:
            old_image = ad.image.path
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            remove_old_img(old_image)
            form.save()
            return redirect('details ad', pk=pk)

    context = {
        'form': AdForm(instance=ad),
        'ad': ad
    }
    return render(request, 'internship/edit_ad.html', context)


@login_required
def delete_ad(request, pk):
    ad = get_current_ad(pk)
    ad.delete()
    return redirect('catalog ads')


@login_required
def deactivate_ad(request, pk):
    ad = get_current_ad(pk)
    ad.is_active = False
    ad.save()
    return redirect('edit ad', pk=pk)


@login_required
def activate_ad(request, pk):
    ad = get_current_ad(pk)
    ad.is_active = True
    ad.save()
    return redirect('edit ad', pk=pk)


@login_required
def apply(request, pk):
    ad = get_current_ad(pk)

    candidate = CandidateProfile.objects.get(user_id=request.user.id)

    form = ApplyForm(request.FILES)

    if request.method == "POST":
        form = ApplyForm(request.POST, request.FILES, instance=candidate)
        if form.is_valid():
            applied_form = form.save(commit=False)
            if not applied_form.CV:
                messages.info(request, 'You have to upload your CV!')
            else:
                new_record = AppliedTracking()
                new_record.CV = applied_form.CV
                new_record.application = ad
                new_record.applied_candidate = candidate
                new_record.save()
                form.save()
                return redirect('home')

    context = {
        'form': form,
        'ad': ad,
        'cv': candidate.CV
    }
    return render(request, 'internship/apply.html', context)


def applied_candidates(request, pk):
    ad = get_current_ad(pk)
    ad_apply_candidates = AppliedTracking.objects.filter(application_id=pk)
    list_of_applied_candidates = get_list_of_applied_candidates(pk)
    num_candidates = len(list_of_applied_candidates)

    context = {
        'candidates': list_of_applied_candidates,
        'ad': ad,
        'records': ad_apply_candidates,
        'num_candidates': num_candidates
    }

    return render(request, 'internship/applied_candidates.html', context)


def about(request):
    return render(request, 'internship/about.html')
