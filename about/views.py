from django.shortcuts import render, get_object_or_404

from profiles.models import UserProfile
from .models import Testimonial


def about(request):
    """
    About Page View
    """
    testimonials = Testimonial.objects.all()
    context = {
            'testimonials': testimonials,
        }
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        context = {
            'testimonials': testimonials,
            'profile': profile,
        }

        return render(request, 'about/about.html', context)
    return render(request, 'about/about.html', context)
