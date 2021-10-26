from django.shortcuts import render, redirect


def view_bag(request):
    """
    A view to return the shopping cart / bag contents
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add product quantities to bag
    """
    # quantity = int(request.POST.get('quantity'))
    
    redirect_url = request.POST.get('redirect_url')
    sizes = None
    if 'ring_sizes' in request.POST:
        sizes = request.POST.getlist('ring_sizes')
        quantity_l = int(request.POST.get('quantity_l'))
        quantity_n = int(request.POST.get('quantity_n'))
        quantity_p = int(request.POST.get('quantity_p'))
        quantity_s = int(request.POST.get('quantity_s'))
        quantity_u = int(request.POST.get('quantity_u'))
        
    # ring_items = request.POST.get('ring_items')
    bag = request.session.get('bag', {})

    if sizes:
        if item_id in list(bag.keys()):
            if sizes in bag[item_id][sizes].keys():
                bag[item_id][sizes] += (
                                                     (['quantity_l'],
                                                      quantity_l),
                                                     (['quantity_n'],
                                                      quantity_n),
                                                     (['quantity_p'],
                                                      quantity_p),
                                                     (['quantity_s'],
                                                      quantity_s),
                                                     (['quantity_u'],
                                                      quantity_u)
                )
                print(sizes)
                print(quantity_u)
            else:
                # bag[item_id] = quantity
                bag[item_id]['ring_items']['quantity_l'] = quantity_l
                bag[item_id]['ring_items']['quantity_n'] = quantity_n
                bag[item_id]['ring_items']['quantity_p'] = quantity_p
                bag[item_id]['ring_items']['quantity_s'] = quantity_s
                bag[item_id]['ring_items']['quantity_u'] = quantity_u
        else:
            bag[item_id] = {sizes:
                            {['quantity_l']: quantity_l,
                             ['quantity_n']: quantity_n,
                             ['quantity_p']: quantity_p,
                             ['quantity_s']: quantity_s,
                             ['quantity_u']: quantity_n
                             }
                            }
        print(sizes)
        print(quantity_u)
    # else:
    #     if item_id in list(bag.keys()):
    #         bag[item_id] += quantity
    #     else:
    #         bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
