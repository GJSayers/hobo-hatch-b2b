from django.shortcuts import render

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

    return render(request, 'about/about.html', context)
