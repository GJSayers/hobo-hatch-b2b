from django.shortcuts import render




def error_404(request, exception):
    """
    Display 404 error message and home link
    """
    return render(request, 'error_handlers/error_404.html')


def error_403(request, exception):
    """
    Display 403 error message and home link
    """
    return render(request, 'error_handlers/error_403.html')


def error_400(request, exception):
    """
    Display 400 error message and home link
    """
    return render(request, 'error_handlers/error_400.html')
