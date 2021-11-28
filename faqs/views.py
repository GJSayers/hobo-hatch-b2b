from django.shortcuts import render, get_object_or_404
from .models import Faqs


def faqs(request):
    """
    Index Page View 
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    faqs = Faqs.objects.all()

    context = {
        'profile': profile,
        'faqs': faqs,
    }

    print("faqs", faqs)

    return render(request, 'faqs/faqs.html', context)
