from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

# Create your test_views here.
from django.views.generic import ListView

from Internship.common.main import get_current_ad, get_list_of_applied_candidates, \
    get_current_company_from_request

from Internship.internship_app.forms import AdForm, ApplyForm
from Internship.internship_app.models import Internship_ad, AppliedTracking
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile
from django.contrib import messages


class Home(ListView):
    model = Internship_ad
    template_name = 'shared/../../templates/main/base.html'
    context_object_name = 'ads'
    paginate_by = 3
    ordering = ['-created_at']


class CatalogCompanies(ListView):
    model = CompanyProfile
    template_name = 'internship/catalog_companies.html'
    context_object_name = 'companies'


def catalog_ad(request):
    active_ads = Internship_ad.objects.filter(is_active=True)

    context = {'ads': active_ads}

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
            return redirect('details ad', ad.pk)

    context = {
        'form': form,
        'company_profile': current_company

    }
    return render(request, 'internship/create_ad.html', context)


def details_ad(request, pk):

    try:
        ad = get_current_ad(pk)
    except ObjectDoesNotExist:
        return redirect('home')

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
    return redirect('company profile', request.user.pk)


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
                form.add_error('CV','You have to upload your CV!')
                messages.info(request, 'You have to upload your CV!')
            else:
                new_record = AppliedTracking()
                # new_record.CV = applied_form.CV
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
    return render(request, 'internship/about.html')
