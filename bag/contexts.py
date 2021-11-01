from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    # delivery = Decimal(settings.STANDARD_DELIVERY_COST)
    
    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        product_type = str(product.product_type)
        size_qty = item_data[product_type]
        if product_type == 'rings':
            size_names = size_qty.keys()
            line_qty = size_qty.values()
            print("size_names", size_names)
            print("line_qty", line_qty)
            # qty_l = size_qty.get("quantity_l")
            # val_qty_l = qty_l * product.product_price
            # qty_n = size_qty.get("quantity_n")
            # val_qty_n = qty_n * product.product_price
            # qty_p = size_qty.get("quantity_p")
            # val_qty_p = qty_p * product.product_price
            # qty_s = size_qty.get("quantity_s")
            # val_qty_s = qty_s * product.product_price
            # qty_u = size_qty.get("quantity_u")
            # val_qty_u = qty_u * product.product_price
            # print("Val L", val_qty_l)
            # print("Val n", val_qty_n)
            # print("Val p", val_qty_p)
            # print("Val s", val_qty_s)
            # print("Val u", val_qty_u)
            # total += size_qty * product.product_price
            bag_items.append({ 
                                    'item_id': item_id,
                                    'product_type': str(product.product_type),
                                    'size_qty': size_qty,
                                    'product': product,
                                })
            print("bag items", bag_items)

    # grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        # 'delivery': delivery,
        # 'grand_total': grand_total,
    }

    return context
