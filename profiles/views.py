from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from products.models import Category
from .models import UserProfile
from .forms import UserProfileForm


from checkout.models import Order


def profile(request):
    """
    Display the client / user profile
    """
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
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
                if user_categories:
                    messages.success(request, 'Details updated successfully')
                else:
                    messages.success(request, 'Thank you for applying to be a stockist, your request will be processed by our team within 1 working day')
                    return render(request, 'home/index.html')

            else:
                messages.error(request, 'Update failed. Please check your form is valid.')
        else:
            form = UserProfileForm(instance=profile)
        orders = profile.orders.all()

        
        context = {
            'profile': profile,
            'categories': categories,
            'permissions_list': permissions_list,
            'form': form,
            'orders': orders,
            'on_profile_page': True,
        }
        template = 'profiles/profile.html'
        return render(request, template, profile)
    template = 'profiles/profile.html'
    return render(request, template)


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
