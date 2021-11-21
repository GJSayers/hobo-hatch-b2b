from django.shortcuts import (render, redirect,
                              reverse, get_object_or_404,)
from django.views.decorators.http import require_POST
from django.utils.datastructures import MultiValueDict
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from bag.contexts import bag_contents

import stripe
import json


# @require_POST
# def cache_checkout_data(request):
#     try:
#         pid = request.POST.get('client')


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        live_bag = bag_contents(request)

        form_data = {
            'buyer_name': request.POST['buyer_name'],
            'buyer_phone': request.POST['buyer_phone'],
            'buyer_email': request.POST['buyer_email'],
            'stockist': request.POST['stockist'],
            'accounts_phone': request.POST['accounts_phone'],
            'accounts_email': request.POST['accounts_email'],
            'address_1': request.POST['address_1'],
            'address_2': request.POST['address_2'],
            'town_or_city': request.POST['town_or_city'],
            'county_or_state': request.POST['county_or_state'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
            'delivery_date': request.POST['delivery_date'],      

        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            print("form valid")
            order = order_form.save()
            for item_id, item_data in bag.items():
                print("bag.items", bag.items())
                try:
                    product = Product.objects.get(id=item_id)
                    if 'knitwear' in item_data:
                        product_type = str(product.product_type)
                        size_qty = item_data[product_type]
                        qty = size_qty.values()
                        line_qty = int(sum(qty))
                        print("order form line_qtys", line_qty)
                        line_total = line_qty * product.product_price
                        print("order form line_total", line_total)
                
                        order_line_item = OrderLineItem(
                                        order=order,
                                        product=product,
                                        product_type=product_type,
                                        lineitem_qty=line_qty,
                                        lineitem_total=line_total,
                                    )
                        print("order_line_item", order_line_item)
                        order_line_item.save()
                
                except Product.DoesNotExist:
                    messages.error(request, (
                        "The product you requested was not found in our \
                             database - Please email the team \
                                 for assistance!"))
                    order.delete()
                    return redirect(reverse('view_bag'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                   reverse('checkout_success', args=[order.order_number]))
        else:
            print(order_form.errors)
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        print("checkout bag", bag)

        if not bag:
            messages.error(request, "There are currently \
                no products in your bag")
            return redirect(reverse('collections'))

        live_bag = bag_contents(request)
        print("live_bag", live_bag)
        total = live_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        print(intent)

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')   
        
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Define what the user sees when they have had a successful checkout
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Thankyou, your order have been successfully placed! \
        #     Order number: {order_number}. An email confirmation \
        #         will be sent to {order.buyer_email}')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)

    # if request.user.is_authenticated:
    #     profile = UserProfile.objects.get(user=request.user)
    #     order.user_profile = profile
    #     # Attach the user's profile to the order
    #     order.save()
    #     # decide whether to save the following - might neeed to be dealt with in a different way
    #     if save_info:
    #         profile_data = {
    #             'buyer_phone': order.buyer_phone,
    #             'buyer_email': order.buyer_email,
    #             'accounts_phone': order.accounts_phone,
    #             'accounts_email': order.accounts_email,
    #             'address_1': order.address_1,
    #             'address_2': order.address_2,
    #             'town_or_city': order.town_or_city,
    #             'county_or_state': order.county_or_state,
    #             'postcode': order.postcode,
    #         }
    #         user_profile_form = UserProfileForm(profile_data, instance=profile)
    #         if user_profile_form.is_valid():
    #             user_profile_form.save()

    #     messages.success(request, f'Thankyou, your order have been successfully placed! \
    #         Order number: {order_number}. An email confirmation \
    #             will be sent to {order.buyer_email}')
