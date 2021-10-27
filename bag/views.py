from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product, Type


def view_bag(request):
    """
    A view to return the shopping cart / bag contents
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add product quantities to bag
    """
    ring = request.POST.get('rings')
    clothing = request.POST.get('knitwear')
    if ring:
        quantity_l = int(request.POST.get('quantity_l'))
        quantity_n = int(request.POST.get('quantity_n'))
        quantity_p = int(request.POST.get('quantity_p'))
        quantity_s = int(request.POST.get('quantity_s'))
        quantity_u = int(request.POST.get('quantity_u'))
        redirect_url = request.POST.get('redirect_url')
        bag = request.session.get('bag', {})
    
    elif clothing:
        quantity_xs = int(request.POST.get('quantity_xs'))
        quantity_sm = int(request.POST.get('quantity_sm'))
        quantity_m = int(request.POST.get('quantity_m'))
        quantity_lg = int(request.POST.get('quantity_lg'))
        quantity_xl = int(request.POST.get('quantity_xl'))
        redirect_url = request.POST.get('redirect_url')
        bag = request.session.get('bag', {})

    else:
        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
        bag = request.session.get('bag', {})

    # if Product.clothing_size_matrix:

    if item_id in list(bag.keys()):
        print("bag keys", list(bag.keys()))
        if ring:
            bag[item_id] += quantity_l
            bag[item_id] += quantity_n
            bag[item_id] += quantity_p
            bag[item_id] += quantity_s
            bag[item_id] += quantity_u

        elif clothing:
            bag[item_id] += quantity_xs
            bag[item_id] += quantity_sm
            bag[item_id] += quantity_m
            bag[item_id] += quantity_lg
            bag[item_id] += quantity_xl

        else:
            bag[item_id] += quantity
    else:
        if ring:
            bag[item_id] = quantity_l
            bag[item_id] = quantity_n
            bag[item_id] = quantity_p
            bag[item_id] = quantity_s
            bag[item_id] = quantity_u

        elif clothing:
            bag[item_id] = quantity_xs
            bag[item_id] = quantity_sm
            bag[item_id] = quantity_m
            bag[item_id] = quantity_lg
            bag[item_id] = quantity_xl

        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
