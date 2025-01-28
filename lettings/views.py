from django.shortcuts import render

from .models import Letting


def lettings_index(request):
    """
    A view function to display a list of all lettings

    :param request: HttpRequest object containing metadata about the request.

    :return: HttpRequest object containing the rendered template with the list of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    A view function to display details of a specific lettings.

    :param request: HttpRequest object containing metadata about the request.
    :param letting_id: The ID of the letting ta retrieve and display.

    :return:HttpRequest object containing the rendered template with the letting details.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
