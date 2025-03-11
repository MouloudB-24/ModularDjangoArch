import logging

import sentry_sdk
from django.shortcuts import render

from .models import Letting

logger = logging.getLogger(__name__)


def lettings_index(request):
    """
    A view function to display a list of all lettings

    :param request: HttpRequest object containing metadata about the request.

    :return: HttpRequest object containing the rendered template with the list of lettings.
    """
    try:
        logger.info('Fetching all lettings models from the database')
        lettings_list = Letting.objects.all()
    except Exception as e:
        logger.error('Error fetching lettings models')
        sentry_sdk.capture_exception(e)
    return render(request, 'lettings/index.html', {'lettings_list': lettings_list})


def letting(request, letting_id):
    """
    A view function to display details of a specific lettings.

    :param request: HttpRequest object containing metadata about the request.
    :param letting_id: The ID of the letting ta retrieve and display.

    :return:HttpRequest object containing the rendered template with the letting details.
    """
    try:
        logger.info('Fetching letting model detail from the database')
        letting = Letting.objects.get(id=letting_id)
    except Exception as e:
        logger.error('Error fetching letting model')
        sentry_sdk.capture_exception(e)
    return render(request, 'lettings/letting.html',
                  {'title': letting.title, 'address': letting.address})
