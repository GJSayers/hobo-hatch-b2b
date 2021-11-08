from django.shortcuts import render


def profile(request):
    """
    Display the client / user profile
    """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context) 
