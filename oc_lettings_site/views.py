from django.shortcuts import render


def index(request):
    """View function to render a home page."""

    return render(request, 'index.html')


def page_not_found(request, exceptions):
    """View function to render a custom 404 error page."""

    return render(request, '404.html', status=404)


def server_error(request):
    """View function to render a custom 500 error page."""

    return render(request, '500.html', status=500)

def trigger_500(request):
    raise Exception('Error 500 voluntary!')
