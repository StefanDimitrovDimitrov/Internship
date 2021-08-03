from django.contrib.postgres.search import SearchVector
from django.template import Library

from Internship.internship_app.forms import SortForm, SearchForm
from Internship.internship_app.models import Internship_ad
from itertools import chain

from Internship.internship_profiles.models import CompanyProfile

register = Library()


@register.inclusion_tag('tags/search_company.html', takes_context=True, )
def search_company(context):
    params = extract_filter_values(context.request.GET)

    company = CompanyProfile.objects.filter(
        is_complete=True).filter(
        company_name__icontains=params['text']
    )

    return {
        'companies': company,
        'search_form': SearchForm(initial=params)
    }


def extract_filter_values(params):
    text = params['text'] if 'text' in params else ''

    return {
        'text': text
    }
