from django.template import Library

from Internship.internship_profiles.models import CandidateProfile, CompanyProfile

register = Library()


@register.inclusion_tag(
    'tags/profile_complete_notification.html', takes_context=True, )
def profile_complete_notification(context):
    if context.request.user.profile == 'Candidate':
        user_id = context.request.user.id
        profile = CandidateProfile.objects.get(user_id=user_id)

        return {
            'is_complete': profile.is_complete,
            'user_id': user_id,
            'profile': context.request.user.profile
        }
    elif context.request.user.profile == 'Company':
        user_id = context.request.user.id
        profile = CompanyProfile.objects.get(user_id=user_id)

        return {
            'is_complete': profile.is_complete,
            'user_id': user_id,
            'profile': context.request.user.profile
        }


