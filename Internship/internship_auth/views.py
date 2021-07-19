from django.contrib.auth import login, logout
from django.shortcuts import render, redirect


# Create your views here.
from Internship.internship_auth.forms import LoginForm, RegisterForm, RegisterFormCandidate, RegisterFormCompany
from Internship.internship_auth.models import InternshipUser
from Internship.internship_profiles.forms import CandidateForm, CompanyForm


def register_candidate(request):
    if request.POST:
        form = RegisterFormCandidate(request.POST)
        profile_form = CandidateForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile_form = profile_form.save(commit=False)
            profile_form.user = user
            profile_form.save()

            login(request, user)
            return redirect('home')
    else:
        form = RegisterFormCandidate()
        form.profile = 'candidate'

    context = {
        'form': form,
    }

    return render(request, 'auth/register candidate.html', context)


def register_company(request):
    if request.POST:
        form = RegisterFormCompany(request.POST)
        profile_form = RegisterFormCompany(request.POST, request.FILES)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile_form = profile_form.save(commit=False)
            profile_form.user = user
            profile_form.save()

            login(request, user)
            return redirect('home')
    else:
        form = RegisterFormCompany()


    context = {
        'form': form,
    }

    return render(request, 'auth/register company.html', context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'auth/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')
