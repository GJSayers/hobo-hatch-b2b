from django.shortcuts import render, get_object_or_404
from model_utils.managers import InheritanceManager
from .models import Testimonial


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
