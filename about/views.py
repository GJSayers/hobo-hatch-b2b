from django.shortcuts import render, request,


def about(request):
    """
    About Page View 
    """

    template = 'about/about.html'

    return render(request, template)
