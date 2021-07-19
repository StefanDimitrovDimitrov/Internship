from django.shortcuts import render, redirect

# Create your views here.
from Internship.internship_app.forms import AdForm
from Internship.internship_app.models import Internship_ad
from Internship.internship_auth.models import InternshipUser
from Internship.internship_profiles.forms import CompanyForm
from Internship.internship_profiles.models import CompanyProfile


def home(request):
    return render(request, 'shared/base.html', )


def catalog(request):
    profiles = InternshipUser.objects.all()

    context = {
        'profiles': profiles
    }

    return render(request, 'shared/catalog.html', context)


def catalog_ad(request):
    ads = Internship_ad.objects.all()

    context = {
        'ads': ads
    }

    return render(request, 'shared/catalog_ad.html', context)


def create_ad(request):
    if request.method == "POST":

        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.profile = request.user
            ad.save()
            form.save()
            return redirect('catalog ads')

    context = {
        'form': AdForm(),
    }
    return render(request, 'shared/create_ad.html', context)
