from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product
from profiles.models import UserProfile


def view_bag(request):
    """
    A view to return the shopping cart / bag contents
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    context = {
        'profile': profile,
    }
    return render(request, 'bag/bag.html', context)


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
                    f'{product.product_name} quantities updated, ({one_size})')
            if beltbag_bumbag:
                bag[item_id][product_type]['one_size'] += one_size
                messages.success(
                    request,
                    f'{product.product_name} quantities updated, ({one_size})')
            if belts:
                bag[item_id][product_type]['one_size'] += one_size
                messages.success(
                    request,
                    f'{product.product_name} quantities updated, ({one_size})')
            if blankets:
                bag[item_id][product_type]['one_size'] += one_size
                messages.success(
                    request,
                    f'{product.product_name} quantities updated, ({one_size})')
            if clothing:
                bag[item_id][product_type]['xs'] += xs
                bag[item_id][product_type]['sm'] += sm
                bag[item_id][product_type]['m'] += m
                bag[item_id][product_type]['lg'] += lg
                bag[item_id][product_type]['xl'] += xl
                messages.success(
                    request,
                    f'{product.product_name} quantities updated, XS, {xs} | SM, {sm} | M, {m} | LG, {lg} | XL, {xl}')
            if rings:
                bag[item_id][product_type]['l'] += l
                bag[item_id][product_type]['n'] += n
                bag[item_id][product_type]['p'] += p
                bag[item_id][product_type]['s'] += s
                bag[item_id][product_type]['u'] += u
                messages.success(
                    request,
                    f'{product.product_name} quantities updated, L, {l} | N, {n} | P, {p} | S, {s} | U, {u}')
                    

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
    print("beltbag_bumbag", beltbag_bumbag)
    belts = request.POST.get('belts')
    print("belts", belts)
    beanie_hats = request.POST.get('beanie_hats')
    print("beanie_hats", beanie_hats)
    blankets = request.POST.get('blankets')
    print("blankets", blankets)
    knitwear = request.POST.get('knitwear')
    print("knitwear", knitwear)
    rings = request.POST.get('rings')
    print("rings", rings)

    if knitwear:
        print("knitwear recognsed")
        xs = int(request.POST.get('xs'))
        sm = int(request.POST.get('sm'))
        m = int(request.POST.get('m'))
        lg = int(request.POST.get('lg'))
        xl = int(request.POST.get('xl'))
        product_qty = [xs, sm, m, lg, xl]
        print("product_qty",  product_qty)
        clothing_line_count = int(sum(product_qty))
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
        clothing_line_count = None
        one_size = None
    elif beltbag_bumbag or belts or beanie_hats or blankets:
        print("other items recognised")
        one_size = int(request.POST.get('one_size'))
        clothing_line_count = None
        ring_line_count = None
    else:
        print("edit not working")
        return redirect(reverse('view_bag'))

    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})

    if clothing_line_count is not None:
        print("clothing_line_count 2", clothing_line_count)
        bag[item_id]['knitwear']['xs'] = xs
        bag[item_id]['knitwear']['sm'] = sm
        bag[item_id]['knitwear']['m'] = m
        bag[item_id]['knitwear']['lg'] = lg
        bag[item_id]['knitwear']['xl'] = xl
        messages.success(
            request,
            f'{product.product_name} quantities updated, XS, {xs} | SM, {sm} | M, {m} | LG, {lg} | XL, {xl}')

    elif ring_line_count is not None:
        bag[item_id]['rings']['l'] = l
        bag[item_id]['rings']['n'] = n
        bag[item_id]['rings']['p'] = p
        bag[item_id]['rings']['s'] = s
        bag[item_id]['rings']['u'] = u
        ring_line_count = ring_line_count
        messages.success(
            request,
            f'{product.product_name} quantities updated, L, {l} | N, {n} | P, {p} | S, {s} | U, {u}')

    elif one_size is not None:
        if beltbag_bumbag:
            bag[item_id]['beltbag_bumbag']['one_size'] = one_size
        elif belts:
            bag[item_id]['belts']['one_size'] = one_size
        elif beanie_hats:
            bag[item_id]['beanie_hats']['one_size'] = one_size
        elif blankets:
            bag[item_id]['blankets']['one_size'] = one_size
        messages.success(
            request,
            f'{product.product_name} quantities updated, One Size: {one_size}')
    else:
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
