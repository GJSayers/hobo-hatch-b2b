from django.shortcuts import render, redirect
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
    size_qty = None
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
        print("clothing_size_qtys", clothing_size_qtys)
        clothing_qty = clothing_size_qtys
        size_qty = clothing_qty

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
        print("ring_size_qtys", ring_size_qtys)
        ring_qty = ring_size_qtys
        size_qty = ring_qty
    bag = request.session.get('bag', {})

    def add_quantities(size_qty, product_type, item_id, bag):
        """
        Identifies which product type is being added to the
        bag to avoid overwriting.
        breaking down the function into sections per size type
        """
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
        add_quantities(ring_size_qtys, product_type, item_id, bag)
        
    elif clothing:
        add_quantities(clothing_size_qtys, product_type, item_id, bag)

    request.session['bag'] = bag
    print("session bag", request.session['bag'])
    return redirect(redirect_url)
