from django.shortcuts import render, redirect

# Create your views here.
from Internship.internship_app.models import Internship_ad
from Internship.internship_profiles.forms import CompanyForm, CandidateForm
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile


def get_company_details(request, pk):
    company = CompanyProfile.objects.get(pk=pk)
    ads = Internship_ad.objects.all()

    company_ads = [a for a in ads if a.company_owner_id == pk]


    context = {
        'info': company,
        'company_ads': company_ads
    }

    return render(request, 'profile/company_profile.html', context)



def edit_company_details(request, pk):
    company = CompanyProfile.objects.get(pk=pk)
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect('details company',pk=pk)

    context = {
        'form': CompanyForm(instance=company),
        'info': company

    }

    return render(request, 'profile/edit_company_profile.html', context)


def delete_company_details(request, pk):
    company = CompanyProfile.objects.get(pk=pk)
    company.delete()
    return redirect('catalog companies')



def get_candidate_details(request, pk):
    candidate = CandidateProfile.objects.get(pk=pk)
    a = candidate.profile_image

    context = {
        'info': candidate
    }

    return render(request, 'profile/candidate_profile.html', context)


def edit_candidate_details(request, pk):
    candidate = CandidateProfile.objects.get(pk=pk)
    if request.method == "POST":
        form = CandidateForm(request.POST, request.FILES, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('details candidate', pk=pk)

    context = {
        'form': CandidateForm(instance=candidate),
        'info': candidate

    }

    return render(request, 'profile/edit_candidate_profile.html', context)


def delete_candidate_details(request, pk):
    candidate = CandidateProfile.objects.get(pk=pk)
    candidate.delete()
    return redirect('home')
