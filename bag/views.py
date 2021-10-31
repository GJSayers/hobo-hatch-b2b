from django.shortcuts import render, redirect
from products.models import Product, Type
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
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    def add_quantities(size_qty, product_type, item_id, bag):
        """
        Identifies which product type is being added to the
        bag to avoid overwriting.
        breaking down the function into sections per size type
        """
        if 'rings' in request.POST:
            product_type = request.POST.get('rings')
        elif 'knitwear' in request.POST:
            product_type = request.POST.get('knitwear')
        bag = request.session.get('bag', {})
        
        if size_qty:
            print(size_qty)
            if item_id in list(bag.keys()):
                if size_qty in bag[item_id][product_type].keys():
                    bag[item_id][product_type] += size_qty
                    print("+=", size_qty)
                else:
                    bag[item_id][product_type] = size_qty
                    print("=", size_qty)
            else:
                bag[item_id] = {product_type: size_qty}
                print("create", size_qty)

    if rings:
        if rings:
            quantity_l = int(request.POST.get('quantity_l'))
            quantity_n = int(request.POST.get('quantity_n'))
            quantity_p = int(request.POST.get('quantity_p'))
            quantity_s = int(request.POST.get('quantity_s'))
            quantity_u = int(request.POST.get('quantity_u'))
            product_type = request.POST.get('rings')
            ring_size_qtys = {
                                'quantity_l': quantity_l,
                                'quantity_n': quantity_n,
                                'quantity_p': quantity_p,
                                'quantity_s': quantity_s,
                                'quantity_u': quantity_u
                            }
            print("ring_size_qtys", ring_size_qtys)
            add_quantities(ring_size_qtys, product_type, item_id, bag)
        
    elif clothing:
        if clothing:
            quantity_xs = int(request.POST.get('quantity_xs'))
            quantity_sm = int(request.POST.get('quantity_sm'))
            quantity_m = int(request.POST.get('quantity_m'))
            quantity_lg = int(request.POST.get('quantity_lg'))
            quantity_xl = int(request.POST.get('quantity_xl'))
            product_type = request.POST.get('knitwear')
            clothing_size_qtys = {
                                'quantity_xs': quantity_xs,
                                'quantity_sm': quantity_sm,
                                'quantity_m': quantity_m,
                                'quantity_lg': quantity_lg,
                                'quantity_xl': quantity_xl
                                }
            print("clothing_size_qtys", clothing_size_qtys)
            add_quantities(clothing_size_qtys, product_type, item_id, bag)

    request.session['bag'] = bag
    print("session bag", request.session['bag'])
    return redirect(redirect_url)
