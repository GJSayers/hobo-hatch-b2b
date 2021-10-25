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
    quantity_l = int(request.POST.get('quantity_l'))
    quantity_n = int(request.POST.get('quantity_n'))
    quantity_p = int(request.POST.get('quantity_p'))
    quantity_s = int(request.POST.get('quantity_s'))
    quantity_u = int(request.POST.get('quantity_u'))
    redirect_url = request.POST.get('redirect_url')
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        # bag[item_id] += quantity
        bag[item_id] += quantity_l
        bag[item_id] += quantity_n
        bag[item_id] += quantity_p
        bag[item_id] += quantity_s
        bag[item_id] += quantity_u
    else:
        # bag[item_id] = quantity
        bag[item_id] = quantity_l
        bag[item_id] = quantity_n
        bag[item_id] = quantity_p
        bag[item_id] = quantity_s
        bag[item_id] = quantity_u

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
