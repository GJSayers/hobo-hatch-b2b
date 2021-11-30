from django.shortcuts import render, get_object_or_404

from profiles.models import UserProfile
from .models import Faqs


def faqs(request):
    """
    Index Page View
    """
    faqs = Faqs.objects.all()
    context = {
            'faqs': faqs,
        }
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        context = {
            'faqs': faqs,
        }

        return render(request, 'faqs/faqs.html', context)
    return render(request, 'faqs/faqs.html', context)
