import logging

import sentry_sdk
from django.shortcuts import render

from .models import Profile

logger = logging.getLogger(__name__)


def profiles_index(request):
    """
    A view function to display a list of all profiles.

    :param request: HttpRequest object containing metadata about the request.

    :return: HttpRequest object containing the rendered template with the list of profiles.
    """
    try:
        logger.info('Fetching all profiles models from the database')
        profiles_list = Profile.objects.all()
    except Exception as e:
        logger.error('Error fetching profiles models')
        sentry_sdk.capture_exception(e)
    return render(request, 'profiles/index.html', {'profiles_list': profiles_list})


def profile(request, username):
    """
   A view function to display details of a specific profiles.

   :param request: HttpRequest object containing metadata about the request.
   :param username: The username of the profile ta retrieve and display.

   :return:HttpRequest object containing the rendered template with the profile details.
   """
    try:
        logger.info('Fetching profile model detail from the database')
        profile = Profile.objects.get(user__username=username)
    except Exception as e:
        logger.error('Error fetching profile model')
        sentry_sdk.capture_exception(e)
    return render(request, 'profiles/profile.html', {'profile': profile})
