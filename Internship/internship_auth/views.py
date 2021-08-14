from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

# Create your test_views here.
from Internship.internship_auth.forms import LoginForm, UserModel, \
    RegisterForm, ChangePassword

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
    form = ChangePassword(user=request.user)
    if request.method == "POST":
        form = ChangePassword(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('candidate profile', pk=pk)

    context = {
        'form': form,
        'user': user
    }

    return render(request, 'profile/change_candidate_credentials.html', context)


@login_required
def change_company_credentials(request, pk):
    user = UserModel.objects.get(pk=pk)
    form = ChangePassword(user=request.user)
    if request.method == "POST":
        form = ChangePassword(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('company profile', pk=pk)

    context = {
        'form': form,
        'user': user
    }

    return render(request, 'profile/change_company_credentials.html', context)
