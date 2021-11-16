from django.shortcuts import render


def faqs(request):
    """
    Index Page View 
    """
    return render(request, 'faqs/faqs.html')
