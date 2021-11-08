from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products. models import Product
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
    # bag = request.session.get('bag', {})
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
            bag[item_id][product_type][size_qty] += [size_qty]
            messages.success(request, f'{product.product_name} has been updated {bag[item_id]}')
        else:
            bag[item_id] = {product_type: size_qty}
            print("create", size_qty)
            messages.success(request, f'{product.product_name} has been added to your bag')

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
    print("edit_bag")
    
    rings = request.POST.get('rings')
    clothing = request.POST.get('knitwear')
    beltbag_bumbag = request.POST.get('beltbag_bumbag')
    belts = request.POST.get('belts')
    beanie_hats = request.POST.get('beanie_hats')
    blankets = request.POST.get('blankets')
    size_qty = request.POST.get('size_qty')
    bag = request.session.get('bag', {})

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

    # bag = request.session.get('bag', {})

    def edit_quantities(size_qty, product_type, item_id, bag):
        """
        Identifies which product type is being added to the
        bag to avoid overwriting.
        breaking down the function into sections per size type
        """
        product = get_object_or_404(Product, pk=item_id)
        size_qty = request.POST.get('size_qty')
        line_qty = request.POST.get('line_qty')
        # qty = list(int(request.POST.get(['qty'])))
        if item_id in list(bag.keys()):
            if line_qty > 0:
                bag[item_id] = {product_type: size_qty}
                messages.success(request, f'{product.product_name} has been updated {bag[item_id]}')
                print("update size", size_qty)
            else:
                bag.pop(item_id)
                messages.success(request, f'{product.product_name} has been removed bag')

        bag = request.session.get('bag', {})

    if rings:
        edit_quantities(ring_size_qtys, product_type, item_id, bag)

    elif clothing:
        edit_quantities(clothing_size_qtys, product_type, item_id, bag)

    elif beltbag_bumbag:
        edit_quantities(universal_qty, product_type, item_id, bag)

    elif belts:
        edit_quantities(universal_qty, product_type, item_id, bag)

    elif blankets:
        edit_quantities(universal_qty, product_type, item_id, bag)

    elif beanie_hats:
        edit_quantities(universal_qty, product_type, item_id, bag)

    request.session['bag'] = bag
    print("session bag", request.session['bag'])
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})
    try:
        
        bag.pop(item_id)
        messages.success(request, f'{product.product_name} has been removed bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'There was an error removing this item: {e}')
        return HttpResponse(status=500)
