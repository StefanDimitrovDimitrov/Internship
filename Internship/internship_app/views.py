import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from Internship.internship_app.forms import AdForm, ApplyForm
from Internship.internship_app.models import Internship_ad, AppliedTracking
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile
from django.contrib import messages

# def home(request):
#     return render(request, 'shared/base.html', )


class Home(ListView):
    model = Internship_ad
    template_name = 'shared/base.html'
    context_object_name = 'ads'
    paginate_by = 3


def catalog_companies(request):
    profiles = CompanyProfile.objects.all()

    context = {
        'profiles': profiles
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
    if request.method == "POST":

        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            user_id = request.user.id
            company = CompanyProfile.objects.get(user_id=user_id)
            ad.company_owner_id = company.user_id
            ad.save()
            form.save()
            return redirect('catalog ads')

    context = {
        'form': AdForm(),
    }
    return render(request, 'internship/create_ad.html', context)


@login_required
def details_ad(request, pk):
    ad = Internship_ad.objects.get(pk=pk)
    apply_info = AppliedTracking.objects.filter(application_id=pk)

    user_id = request.user.id



    # candidates = ad.applied_candidates.all()
    context = {
        'ad': ad,
        'id': user_id,
        'candidates': apply_info
    }

    return render(request, 'internship/details.html', context)


@login_required
def edit_ad(request, pk):
    ad = Internship_ad.objects.get(pk=pk)
    old_image = ad.image
    if request.method == "POST":
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            if old_image:
                os.remove(old_image.path)
            form.save()
            return redirect('details ad', pk=pk)

    context = {
        'form': AdForm(instance=ad),
        'ad': ad
    }
    return render(request, 'internship/edit.html', context)


@login_required
def delete_ad(request, pk):
    ad = Internship_ad.objects.get(pk=pk)
    ad.delete()
    return redirect('catalog ads')


@login_required
def deactivate_ad(request, pk):
    ad = Internship_ad.objects.get(pk=pk)
    ad.is_active = False
    ad.save()
    return redirect('catalog ads')


@login_required
def activate_ad(request, pk):
    ad = Internship_ad.objects.get(pk=pk)
    ad.is_active = True
    ad.save()
    return redirect('catalog ads')


def alert(param):
    return param


@login_required
def apply(request, pk):
    ad = Internship_ad.objects.get(pk=pk)
    candidate = CandidateProfile.objects.get(user_id=request.user.id)
    form = ApplyForm(request.FILES,instance=candidate)
    CV = candidate.CV

    if request.method == "POST":
        form = ApplyForm(request.POST, request.FILES,instance=candidate)
        if form.is_valid():
            applied_form = form.save(commit=False)
            if not applied_form.CV:
                messages.info(request,'You have to upload your CV!')
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
    }
    return render(request, 'internship/apply.html', context)
