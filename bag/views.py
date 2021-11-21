from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product
# from django.utils.datastructures import MultiValueDict


def view_bag(request):
    """
    A view to return the shopping cart / bag contents
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add product quantities to bag
    """
    rings = request.POST.get('rings')
    clothing = request.POST.get('knitwear')
    beltbag_bumbag = request.POST.get('beltbag_bumbag')
    belts = request.POST.get('belts')
    beanie_hats = request.POST.get('beanie_hats')
    blankets = request.POST.get('blankets')
    redirect_url = request.POST.get('redirect_url')

    if 'knitwear' in request.POST:
        xs = int(request.POST.get('xs'))
        sm = int(request.POST.get('sm'))
        m = int(request.POST.get('m'))
        lg = int(request.POST.get('lg'))
        xl = int(request.POST.get('xl'))
        product_type = request.POST.get('knitwear')
        clothing_size_qtys = {
                            'xs': xs,
                            'sm': sm,
                            'm': m,
                            'lg': lg,
                            'xl': xl
                            }

    elif 'rings' in request.POST:
        l = int(request.POST.get('l'))
        n = int(request.POST.get('n'))
        p = int(request.POST.get('p'))
        s = int(request.POST.get('s'))
        u = int(request.POST.get('u'))
        product_type = request.POST.get('rings')
        ring_size_qtys = {
                            'l': l,
                            'n': n,
                            'p': p,
                            's': s,
                            'u': u
                        }

    elif 'beltbag_bumbag' in request.POST:
        one_size = int(request.POST.get('one_size'))
        product_type = request.POST.get('beltbag_bumbag')
        universal_qty = {'one_size': one_size}

    elif 'belts' in request.POST:
        one_size = int(request.POST.get('one_size'))
        product_type = request.POST.get('belts')
        universal_qty = {'one_size': one_size}

    elif 'beanie_hats' in request.POST:
        one_size = int(request.POST.get('one_size'))
        product_type = request.POST.get('beanie_hats')
        universal_qty = {'one_size': one_size}

    elif 'blankets' in request.POST:
        one_size = int(request.POST.get('one_size'))
        product_type = request.POST.get('blankets')
        universal_qty = {'one_size': one_size}

    bag = request.session.get('bag', {})

    def add_quantities(size_qty, product_type, item_id, bag):
        """
        Identifies which product type is being added to the
        bag to avoid overwriting.
        breaking down the function into sections per size type
        """
        product = get_object_or_404(Product, pk=item_id)

        if item_id in list(bag.keys()):
            if beanie_hats:
                bag[item_id][product_type]['one_size'] += one_size
                messages.success(
                    request,
                    f'{product.product_name} has been updated {bag[item_id]}')
            if beltbag_bumbag:
                bag[item_id][product_type]['one_size'] += one_size
                messages.success(
                    request,
                    f'{product.product_name} has been updated {bag[item_id]}')
            if belts:
                bag[item_id][product_type]['one_size'] += one_size
                messages.success(
                    request,
                    f'{product.product_name} has been updated {bag[item_id]}')
            if blankets:
                bag[item_id][product_type]['one_size'] += one_size
                messages.success(
                    request,
                    f'{product.product_name} has been updated {bag[item_id]}')
            if clothing:
                bag[item_id][product_type]['xs'] += xs
                bag[item_id][product_type]['sm'] += sm
                bag[item_id][product_type]['m'] += m
                bag[item_id][product_type]['lg'] += lg
                bag[item_id][product_type]['xl'] += xl
                messages.success(
                    request,
                    f'{product.product_name} has been updated {bag[item_id]}')
            if rings:
                bag[item_id][product_type]['l'] += l
                bag[item_id][product_type]['n'] += n
                bag[item_id][product_type]['p'] += p
                bag[item_id][product_type]['s'] += s
                bag[item_id][product_type]['u'] += u
                messages.success(
                    request,
                    f'{product.product_name} has been updated {bag[item_id]}')

        else:
            bag[item_id] = {product_type: size_qty}
            print("create", size_qty)
            messages.success(
                request,
                f'{product.product_name} has been added to your bag')

    if rings:
        add_quantities(ring_size_qtys, product_type, item_id, bag)

    elif clothing:
        add_quantities(clothing_size_qtys, product_type, item_id, bag)

    elif beltbag_bumbag:
        add_quantities(universal_qty, product_type, item_id, bag)

    elif belts:
        add_quantities(universal_qty, product_type, item_id, bag)

    elif blankets:
        add_quantities(universal_qty, product_type, item_id, bag)

    elif beanie_hats:
        add_quantities(universal_qty, product_type, item_id, bag)

    request.session['bag'] = bag
    print("session bag", request.session['bag'])
    return redirect(redirect_url)


def edit_bag(request, item_id):
    """
    Edit or remove items from the bag view
    """
    print("edit_bag", edit_bag)
    beltbag_bumbag = request.POST.get('beltbag_bumbag')
    belts = request.POST.get('belts')
    beanie_hats = request.POST.get('beanie_hats')
    blankets = request.POST.get('blankets')
    knitwear = request.POST.get('knitwear')
    rings = request.POST.get('rings')

    if knitwear:
        print("knitwear recognsed")
        xs = int(request.POST.get('xs'))
        sm = int(request.POST.get('sm'))
        m = int(request.POST.get('m'))
        lg = int(request.POST.get('lg'))
        xl = int(request.POST.get('xl'))
        product_qty = [xs, sm, m, lg, xl]
        print("product_qty",  product_qty)
        clothing_line_count = sum(product_qty)
        print("clothing_line_count", clothing_line_count)
        ring_line_count = None
        one_size = None
    elif rings:
        print("rings recognised")
        l = int(request.POST.get('l'))
        n = int(request.POST.get('n'))
        p = int(request.POST.get('p'))
        s = int(request.POST.get('s'))
        u = int(request.POST.get('u'))
        product_qty = [l, n, p, s, u]
        print("product_qty",  product_qty)
        ring_line_count = sum(product_qty)
        print("ring_line_count", ring_line_count)
        clothing_line_count = 0
        one_size = 0
    elif beltbag_bumbag or belts or beanie_hats or blankets:
        print("other items recognised")
        one_size = int(request.POST.get('one_size'))
        clothing_line_count = 0
        ring_line_count = 0
    else:
        print("edit not working")
        return redirect(reverse('view_bag'))

    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})

    # if clothing_line_count > 0:
    if clothing_line_count > 0:
        bag[item_id]['xs'] = xs
        bag[item_id]['sm'] = sm
        bag[item_id]['m'] = m
        bag[item_id]['lg'] = lg
        bag[item_id]['xl'] = xl
        messages.success(
            request,
            f'{product.product_name} quantities updated {bag[item_id]}')
    else:
        if clothing_line_count == 0:
            bag.pop(item_id)

    # if ring_line_count is not None:
    if ring_line_count > 0:
        bag[item_id]['l'] = l
        bag[item_id]['n'] = n
        bag[item_id]['p'] = p
        bag[item_id]['s'] = s
        bag[item_id]['u'] = u
        messages.success(
            request,
            f'{product.product_name} quantities updated {bag[item_id]}')
    else:
        if ring_line_count == 0:
            bag.pop(item_id)
        messages.success(
            request,
            f'{product.product_name} has been removed from your bag')

    # if one_size is not None:
    if one_size > 0:
        bag[item_id]['one_size'] = one_size
        messages.success(
            request,
            f'{product.product_name} quantities updated {bag[item_id]}')
    else:
        if one_size == 0:
            bag.pop(item_id)
        messages.success(
            request,
            f'{product.product_name} has been removed from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})
    try:
        bag.pop(item_id)
        messages.success(
            request,
            f'{product.product_name} has been removed bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(
            request,
            f'There was an error removing this item: {e}')
        return HttpResponse(status=500)
