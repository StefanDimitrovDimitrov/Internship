from django.template import Library

from Internship.internship_app.forms import SortForm, SearchForm
from Internship.internship_app.models import Internship_ad
from django.db.models import Q

register = Library()


@register.inclusion_tag('tags/sort_ads.html', takes_context=True, )
def sort_ads(context):
    params = extract_filter_values(context.request.GET)

    ads = Internship_ad.objects.filter(
        Q(city__icontains=params['city']) &
        Q(field__icontains=params['field']) &
        Q(duration__icontains=params['duration']) &
        Q(employment_type__icontains=params['employment_type']) &(
             Q(title__icontains=params['text']) |
             Q(company_owner__company_name__icontains=params['text']) |
             Q(city__icontains=params['text']) |
             Q(field__icontains=params['text']) |
             Q(duration__icontains=params['text']) |
             Q(employment_type__icontains=params['text'])
         )
    ).filter(is_active=True).order_by('-created_at')

    count_ads = ads.count()

    return {
        'ads': ads,
        'count_ads': count_ads,
        'sort_form': SortForm(initial=params),
        'search_form': SearchForm(initial=params),
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
