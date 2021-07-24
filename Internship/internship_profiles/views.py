from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from Internship.internship_app.models import Internship_ad
from Internship.internship_auth.forms import RegisterFormCandidate, RegisterFormCompany
from Internship.internship_profiles.forms import CompanyForm, CandidateForm
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile

UserModel = get_user_model()


def get_company_details(request, pk):
    company = CompanyProfile.objects.get(pk=pk)
    ads = Internship_ad.objects.all()

    company_ads = [a for a in ads if a.company_owner_id == pk]

    context = {
        'info': company,
        'company_ads': company_ads
    }

    return render(request, 'profile/company_profile.html', context)


@login_required
def edit_company_details(request, pk):
    company = CompanyProfile.objects.get(pk=pk)
    if request.method == "POST":
        profile_form = CompanyForm(request.POST, request.FILES, instance=company)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('details company', pk=pk)

    context = {
        'form': CompanyForm(instance=company),
        'info': company,
    }

    return render(request, 'profile/edit_company_profile.html', context)


def change_company_credentials(request, pk):
    user = UserModel.objects.get(pk=pk)
    company_profile = CompanyProfile.objects.get(user_id=pk)
    if request.method == "POST":
        form = RegisterFormCompany(request.POST, instance=user)
        if form.is_valid():
            temp_object = form.save(commit=False)
            company_profile.company_name = temp_object.company_name
            company_profile.email = temp_object.email
            company_profile.save()
            temp_object = form.save()
            login(request, user)
            return redirect('details company', pk=pk)

    context = {
        'form': RegisterFormCompany(instance=user),
        'user': user
    }

    return render(request, 'profile/change_company_credentials.html', context)


def delete_company_details(request, pk):
    company = CompanyProfile.objects.get(pk=pk)
    company.delete()
    return redirect('catalog companies')


def get_candidate_details(request, pk):
    candidate = CandidateProfile.objects.get(pk=pk)
    ads = Internship_ad.objects.all()

    list_of_ads = []
    for ad in ads:
        candidates = ad.applied_candidates.all()
        for c in candidates:
            if c.user_id == candidate.user_id:
                list_of_ads.append(ad)



    context = {
        'info': candidate,
        'applied_ads': list_of_ads
    }

    return render(request, 'profile/candidate_profile.html', context)


def edit_candidate_details(request, pk):
    candidate = CandidateProfile.objects.get(pk=pk)
    if request.method == "POST":
        profile_form = CandidateForm(request.POST, request.FILES, instance=candidate)

        if profile_form.is_valid():
            profile_form.save()
            return redirect('details candidate', pk=pk)

    context = {
        'profile_form': CandidateForm(instance=candidate),
        'info': candidate,
    }

    return render(request, 'profile/edit_candidate_profile.html', context)


def change_candidate_credentials(request, pk):
    user = UserModel.objects.get(pk=pk)
    candidate_profile = CandidateProfile.objects.get(user_id=pk)
    if request.method == "POST":
        form = RegisterFormCandidate(request.POST, instance=user)
        if form.is_valid():
            temp_object = form.save(commit=False)
            candidate_profile.email = temp_object.email
            candidate_profile.save()
            temp_object = form.save()
            login(request, user)
            return redirect('details candidate', pk=pk)

    context = {
        'form': RegisterFormCandidate(instance=user),
        'user': user
    }

    return render(request, 'profile/change_candidate_credentials.html', context)


def delete_candidate_details(request, pk):
    candidate = CandidateProfile.objects.get(pk=pk)
    candidate.delete()
    return redirect('home')
