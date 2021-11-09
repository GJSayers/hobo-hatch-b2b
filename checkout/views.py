from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There are no items in your bag")
        return redirect(reverse('collections'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JbmpZIUgibpskr7X5tNRtkv4gFcmpQq30UebEZPWjzrjJYEdhZ2kYr6svKfwPPLn75JSzPbqYMUTLgamYtiV39l0081BdcCI0',
        'CLIENT_SECRET': 'test client secret'
    }

    return render(request, template, context)
