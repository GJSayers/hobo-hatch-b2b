from django.shortcuts import (render, redirect,
                              reverse, get_object_or_404,)
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.contrib import messages
from django.conf import settings

import stripe
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import bag_contents
from .forms import OrderForm
from .models import Order, OrderLineItem


def checkout(request):
    """
    Sends a request to stripe to make a purchase
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        """
        Retreives the posted form data and bag/ purchase data
        """
        bag = request.session.get('bag', {})
        live_bag = bag_contents(request)
        profile = UserProfile.objects.get(user=request.user)

        form_data = {
            'stockist': profile,
            'buyer_name': request.POST['buyer_name'],
            'buyer_phone': request.POST['buyer_phone'],
            'buyer_email': request.POST['buyer_email'],
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
            """
            Checks id the order form data is valid
            Saves buyer data if box is checked
            """
            order = order_form.save()
            for item_id, item_data in bag.items():
                """
                Iterates through items in bag
                Assigns size qtys & lineqty
                """
                try:
                    product = Product.objects.get(id=item_id)
                    product_type = str(product.product_type)
                    size_qty = item_data[product_type]
                    qty = size_qty.values()
                    xs_l_one_size = list(qty)[0]
                    if product_type != 'rings' and product_type != 'knitwear':
                        sm_n = 0
                        m_p = 0
                        lg_s = 0
                        xl_u = 0
                    else:
                        sm_n = list(qty)[1]
                        m_p = list(qty)[2]
                        lg_s = list(qty)[3]
                        xl_u = list(qty)[4]

                    line_qty = int(sum(qty))
                    line_total = line_qty * product.product_price
                    order_line_item = OrderLineItem(
                                    order=order,
                                    product=product,
                                    product_type=product_type,
                                    xs_l_one_size=xs_l_one_size,
                                    sm_n=sm_n,
                                    m_p=m_p,
                                    lg_s=lg_s,
                                    xl_u=xl_u,
                                    lineitem_qty=line_qty,
                                    lineitem_total=line_total,
                                )
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
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})

        if not bag:
            messages.error(request, "There are currently \
                no products in your bag")
            return redirect(reverse('collections'))

        live_bag = bag_contents(request)
        total = live_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'buyer_name': profile.user.get_full_name(),
                    'buyer_email': profile.user.email,
                    'buyer_phone': profile.buyer_phone,
                    'stockist': profile,
                    'accounts_phone': profile.accounts_phone,
                    'accounts_email': profile.accounts_email,
                    'address_1': profile.address_1,
                    'address_2': profile.address_2,
                    'town_or_city': profile.town_or_city,
                    'county_or_state': profile.county_or_state,
                    'postcode': profile.postcode,
                    'country': profile.country,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'profile': profile,
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def send_confirmation_email(request, order):
    """
    Send the user a confirmation email
    """
    cust_email = order.buyer_email
    subject = render_to_string(
        'checkout/confirmation_emails/confirmation_email_subject.txt',
        {'order': order})
    body = render_to_string(
        'checkout/confirmation_emails/confirmation_email_body.txt',
        {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )


def checkout_success(request, order_number):
    """
    Define what the user sees when they have had a successful checkout
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order = get_object_or_404(Order, order_number=order_number)
        order.save()
        if save_info:
            profile_data = {
                'buyer_name': order.buyer_name,
                'buyer_phone': order.buyer_phone,
                'buyer_email': order.buyer_email,
                'accounts_phone': order.accounts_phone,
                'accounts_email': order.accounts_email,
                'address_1': order.address_1,
                'address_2': order.address_2,
                'town_or_city': order.town_or_city,
                'county_or_state': order.county_or_state,
                'postcode': order.postcode,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

            send_confirmation_email(request, order=order)

        messages.success(request, f'Thankyou, your order has been successfully placed! \
            Order number: {order_number}. An email confirmation \
                will be sent to {order.buyer_email}')

        if 'bag' in request.session:
            del request.session['bag']

        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
        }

    return render(request, template, context)
