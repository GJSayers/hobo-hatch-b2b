from django.shortcuts import render, get_object_or_404

from profiles.models import UserProfile

def index(request):
    """
    Index Page View
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    context = {
        'profile': profile,
    }

    return render(request, 'home/index.html', context)
