from django.shortcuts import render
from .models import Testimonial
from profiles.models import UserProfile


def about(request):
    """
    About Page View 
    """
    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
        # 'buyer': buyer,
        
    }
    print("testimonials", testimonials)
    # print("buyer", buyer)
    


    return render(request, 'about/about.html', context)
