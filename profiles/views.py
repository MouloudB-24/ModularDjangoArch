from django.shortcuts import render

from .models import Profile


def profiles_index(request):
    """
    A view function to display a list of all profiles.

    :param request: HttpRequest object containing metadata about the request.

    :return: HttpRequest object containing the rendered template with the list of profiles.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
   A view function to display details of a specific profiles.

   :param request: HttpRequest object containing metadata about the request.
   :param username: The username of the profile ta retrieve and display.

   :return:HttpRequest object containing the rendered template with the profile details.
   """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
