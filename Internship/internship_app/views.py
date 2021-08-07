import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from Internship.common.main import get_current_company, get_current_ad, get_list_of_applied_candidates, \
    get_list_active_ads, get_current_company_from_request
from Internship.common.main import remove_old_img
from Internship.internship_app.forms import AdForm, ApplyForm
from Internship.internship_app.models import Internship_ad, AppliedTracking
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile
from django.contrib import messages


class Home(ListView):
    model = Internship_ad
    template_name = 'shared/../../templates/main/base.html'
    context_object_name = 'ads'
    paginate_by = 3


def catalog_companies(request):
    companies = CompanyProfile.objects.filter(is_complete=True).order_by('company_name')

    context = {
        'companies': companies
    }

    return render(request, 'internship/catalog_companies.html', context)


def catalog_ad(request):
    active_ads = get_list_active_ads()

    context = {
        'ads': active_ads
    }

    return render(request, 'internship/catalog_ads.html', context)


@login_required
def create_ad(request):
    current_company = get_current_company_from_request(request)
    form = AdForm()
    if request.method == "POST":

        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.company_owner = current_company
            ad.save()
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

    if request.method == "POST":

        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
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
                new_record.internship_ads = ad
                new_record.applied_candidates = candidate
                new_record.save()
                return redirect('candidate profile', request.user.pk)

    context = {
        'form': form,
        'ad': ad,
        'cv': candidate.CV
    }
    return render(request, 'internship/apply.html', context)



def about(request):
    records = AppliedTracking.objects.all()

    for record in records:

        ads_list = record.internship_ads.title
        candidates = record.applied_candidates.email


    return render(request, 'internship/about.html')
