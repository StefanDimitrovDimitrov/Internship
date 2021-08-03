from django.contrib.postgres.search import SearchVector
from django.template import Library

from Internship.internship_app.forms import SortForm, SearchForm
from Internship.internship_app.models import Internship_ad
from itertools import chain

register = Library()


@register.inclusion_tag('tags/sort_ads.html', takes_context=True, )
def sort_ads(context):
    params = extract_filter_values(context.request.GET)

    ads_list1 = Internship_ad.objects.filter(
        city__icontains=params['city'],
        field__icontains=params['field'],
        duration__icontains=params['duration'],
        employment_type__icontains=params['employment_type'],
        title__icontains=params['text']

    )
    ads_list2 = Internship_ad.objects.filter(
        city__icontains=params['city'],
        field__icontains=params['field'],
        duration__icontains=params['duration'],
        employment_type__icontains=params['employment_type'],
        company_owner__company_name__icontains=params['text']
    )

    ads = set(chain(ads_list1, ads_list2))

    return {
        'ads': ads,
        'sort_form': SortForm(initial=params),
        'search_form': SearchForm(initial=params)
    }


def extract_filter_values(params):
    city = params['city'] if 'city' in params else ''
    field = params['field'] if 'field' in params else ''
    duration = params['duration'] if 'duration' in params else ''
    employment_type = params['employment_type'] if 'employment_type' in params else ''
    text = params['text'] if 'text' in params else ''

    return {
        'city': city,
        'field': field,
        'duration': duration,
        'employment_type': employment_type,
        'text': text
    }
