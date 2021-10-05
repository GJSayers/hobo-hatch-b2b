from django.shortcuts import render


def index(request):
    """
    Index Page View 
    """
    return render(request, 'home/index.html')
