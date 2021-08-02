import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from Internship.comman.main import get_current_company
from Internship.comman.remove_old_img import remove_old_img
from Internship.internship_app.forms import AdForm, ApplyForm
from Internship.internship_app.models import Internship_ad, AppliedTracking
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile
from django.contrib import messages


# def home(request):
#     return render(request, 'shared/base.html', )
# class Home(SingleObjectMixin, ListView):
#     model = Internship_ad
#     template_name = 'shared/base.html'
#
#     object = None
#
#     paginate_by = 3
#
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object(queryset=Internship_ad.objects.all())
#         return super().get(request, *args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['source'] = self.object
#         return context
#
#     def get_queryset(self):
#         return self.object.ads_set.all()

class Home(ListView):
    model = Internship_ad
    template_name = 'shared/base.html'
    context_object_name = 'ads'
    paginate_by = 3


def catalog_companies(request):
    companies = CompanyProfile.objects.filter(is_complete=True)

    context = {
        'companies': companies
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
    current_company = get_current_company(request)
    if request.method == "POST":

        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.company_owner_id = current_company.user_id
            ad.save()
            form.save()
            return redirect('catalog ads')

    context = {
        'form': AdForm(),
        'company_profile': current_company

    }
    return render(request, 'internship/create_ad.html', context)



def details_ad(request, pk):

    ad = Internship_ad.objects.get(pk=pk)
    ad_apply_candidates = AppliedTracking.objects.filter(application_id=pk)
    all_candidates = CandidateProfile.objects.all()
    list_of_applied_candidates = [c for c in all_candidates for record in ad_apply_candidates if
                                  c.user_id == record.applied_candidate_id]
    companies = CompanyProfile.objects.all()
    company_owner = [company for company in companies if company.user_id == ad.company_owner_id][0]

    list_of_applied_candidates = set(list_of_applied_candidates)

    if request.user:
        user_id = request.user.id
        context = {
        'ad': ad,
        'id': user_id,
        'candidates': list_of_applied_candidates,
        'list_applied_cv': ad_apply_candidates,
        'company_owner': company_owner
        }
    else:
        context = {
            'ad': ad,
            'candidates': list_of_applied_candidates,
            'list_applied_cv': ad_apply_candidates,
            'company_owner': company_owner
        }

    # candidates = ad.applied_candidates.all()


    return render(request, 'internship/details_ad.html', context)


@login_required
def edit_ad(request, pk):
    ad = Internship_ad.objects.get(pk=pk)
    old_image = ''
    if request.method == "POST":
        if ad.image:
            old_image = ad.image.path
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            remove_old_img(old_image)
            form.save()
            return redirect('details ad', pk=pk)

    context = {
        'form': AdForm(instance=ad),
        'ad': ad
    }
    return render(request, 'internship/edit_ad.html', context)


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
    form = ApplyForm(request.FILES)
    CV = candidate.CV

    if request.method == "POST":
        form = ApplyForm(request.POST, request.FILES, instance=candidate)
        if form.is_valid():
            applied_form = form.save(commit=False)
            if not applied_form.CV:
                messages.info(request, 'You have to upload your CV!')
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
        'cv': CV
    }
    return render(request, 'internship/apply.html', context)

def applied_candidates(request, pk):
    ad = Internship_ad.objects.get(pk=pk)
    ad_apply_candidates = AppliedTracking.objects.filter(application_id=pk)
    all_candidates = CandidateProfile.objects.all()
    list_of_applied_candidates = [c for c in all_candidates for record in ad_apply_candidates if
                                  c.user_id == record.applied_candidate_id]




    context ={
        'candidates':list_of_applied_candidates,
        'ad': ad,
        'records':ad_apply_candidates,
    }

    return render(request, 'internship/applied_candidates.html', context)