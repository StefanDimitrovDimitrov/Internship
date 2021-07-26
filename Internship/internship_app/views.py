
import os


from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from Internship.internship_app.forms import AdForm, ApplyForm
from Internship.internship_app.models import Internship_ad
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile


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

    return render(request, 'catalog_companies.html', context)


def catalog_ad(request):
    list_all_ads = Internship_ad.objects.all()

    ads = [ad for ad in list_all_ads if ad.is_active]

    context = {
        'ads': ads
    }

    return render(request, 'catalog_ads.html', context)


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
    return render(request, 'create_ad.html', context)


def details_ad(request, pk):
    ad = Internship_ad.objects.get(pk=pk)
    user_id = request.user.id
    candidates = ad.applied_candidates.all()
    context = {
        'ad': ad,
        'id': user_id,
        'candidates': candidates
    }

    return render(request, 'details.html', context)


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
    return render(request, 'edit.html', context)


def delete_ad(request, pk):
    ad = Internship_ad.objects.get(pk=pk)
    ad.delete()
    return redirect('catalog ads')


def deactivate_ad(request, pk):
    ad = Internship_ad.objects.get(pk=pk)
    ad.is_active = False
    ad.save()
    return redirect('catalog ads')

def activate_ad(request, pk):
    ad = Internship_ad.objects.get(pk=pk)
    ad.is_active = True
    ad.save()
    return redirect('catalog ads')


def apply(request, pk):
    ad = Internship_ad.objects.get(pk=pk)
    user_id = request.user.id

    candidate = CandidateProfile.objects.get(user_id=user_id)
    form = ApplyForm(request.FILES)

    if request.method == "POST":
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            applied_form = form.save(commit=False)
            return redirect('home')

    context = {
        'form': ApplyForm(instance=candidate),
        'ad': ad
    }
    return render(request, 'apply.html', context)
