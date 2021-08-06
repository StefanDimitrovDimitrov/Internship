from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from Internship.internship_auth.forms import LoginForm, UserModel, \
    RegisterForm

from Internship.internship_profiles.models import CompanyProfile, CandidateProfile


def register_candidate(request):
    """
    form_save is trigger a post save type signal. Which is responsible of creating Candidate Profile.
    Check internship_profiles/signals.py for more details
    """

    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            candidate_user = form.save(commit=False)
            candidate_user.profile = "Candidate"
            candidate_user = form.save()
            login(request, candidate_user)
            return redirect('candidate profile', pk=request.user.pk)

    return render(request, 'auth/register candidate.html', context={"form": form})


def register_company(request):
    """
    form_save is trigger a post save type signal. Which is responsible of creating Company Profile.
    Check internship_profiles/signals.py for more details
    """

    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            company_user = form.save(commit=False)
            company_user.profile = "Company"
            company_user = form.save()
            login(request, company_user)
            return redirect('company profile', pk=request.user.pk)

    context = {
        "form": form,
    }

    return render(request, 'auth/register company.html', context)


def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'auth/login.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('home')


@login_required
def change_candidate_credentials(request, pk):
    user = UserModel.objects.get(pk=pk)
    candidate_profile = CandidateProfile.objects.get(user_id=pk)
    if request.method == "POST":
        form = RegisterForm(request.POST, instance=user)
        if form.is_valid():
            temp_object = form.save(commit=False)
            candidate_profile.email = temp_object.email
            candidate_profile.save()
            temp_object.save()
            login(request, user)
            return redirect('candidate profile', pk=pk)

    context = {
        'form': RegisterForm(instance=user),
        'user': user
    }

    return render(request, 'profile/change_candidate_credentials.html', context)


@login_required
def change_company_credentials(request, pk):
    user = UserModel.objects.get(pk=pk)
    company_profile = CompanyProfile.objects.get(pk=pk)
    if request.method == "POST":
        form = RegisterForm(request.POST, instance=user)
        if form.is_valid():
            temp_object = form.save(commit=False)
            company_profile.email = temp_object.email
            company_profile.save()
            temp_object.save()
            login(request, user)
            return redirect('company profile', pk=pk)

    context = {
        'form': RegisterForm(instance=user),
        'user': user
    }

    return render(request, 'profile/change_company_credentials.html', context)
