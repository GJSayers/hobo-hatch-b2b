from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    rings = request.POST.get('rings')
    clothing = request.POST.get('knitwear')
    bag = request.session.get('bag', {})
    delivery = Decimal(settings.STANDARD_DELIVERY_COST)

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        product_type = str(product.product_type)
        size_qty = item_data[product_type]
        print(size_qty)
        print(item_data)
        size_names = size_qty.keys()
        qty = size_qty.values()
        line_qty = sum(size_qty.values())
        line_total = line_qty * product.product_price
        print("line_qty", line_qty)
        print("qty", qty)
        # total += qty * product.product_price
        bag_items.append({ 
                                'item_id': item_id,
                                'product_type': str(product.product_type),
                                'qty': qty,
                                'size_names': size_names,
                                'line_qty': line_qty,
                                'line_total': line_total,
                                'product': product,
                            })
        #     print("bag items", bag_items)
        # else:
        #     product = get_object_or_404(Product, pk=item_id)
        #     # size_names = size_qty.keys()
        #     qty = item_data
        #     line_qty = sum(size_qty.values())
        #     line_total = line_qty * product.product_price
        #     bag_items.append({ 
        #                         'item_id': item_id,
        #                         'product_type': str(product.product_type),
        #                         'qty': qty,
        #                         # 'size_names': size_names,
        #                         'line_qty': line_qty,
        #                         'line_total': line_total,
        #                         'product': product,
        #     })
        # print("bag items", bag_items)


    # grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'delivery': delivery,
        # 'total': total,
        # 'grand_total': grand_total
    }

    return context
