from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from products.models import Category
from .models import UserProfile
from .forms import UserProfileForm


from checkout.models import Order


def profile(request):
    """
    Display the client / user profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    user_categories = profile.categories
    permissions_list = user_categories[0:]
    print("permissions_list", permissions_list)
    categories = Category.objects.all()
    permissions_categories = Category.objects.filter(
                                          name__in=permissions_list)
    form = UserProfileForm(instance=profile)
    print("profile", profile)
    print("profile", profile.user)
    print("profile", profile.stockist)
    print("profile", profile.buyer_name)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Details updated successfully')
        else:
            messages.error(request, 'Update failed. Polease check your form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'categories': categories,
        'permissions_list': permissions_list,
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context) 


def order_history(request, order_number):
    
    order = get_object_or_404(Order, order_number=order_number)
    order_date = order.date

    messages.info(request, (
        f'This order was placed on {order_date}, this is a copy of order number {{order_number|truncatechars:6}}the confirmation generated at the time of purchase.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
