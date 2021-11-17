from django.shortcuts import render
from .models import Faqs


def faqs(request):
    """
    Index Page View 
    """
    faqs = Faqs.objects.all()

    context = {
        'faqs': faqs,
    }

    print("faqs", faqs)

    return render(request, 'faqs/faqs.html', context)
