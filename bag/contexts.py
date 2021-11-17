from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    line_totals = []
    # size_qty = []
    # total = 0
    # product_count = 0
    # rings = request.POST.get('rings')
    # clothing = request.POST.get('knitwear')
    bag = request.session.get('bag', {})
    delivery = Decimal(settings.STANDARD_DELIVERY_COST)

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        print("contexts product", product)
        product_type = str(product.product_type)
        print("contexts product_type", product_type)
        size_qty = item_data[product_type]
        print("contexts size_qty", size_qty)
        size_items = size_qty.items()
        print("contexts size_items", size_items)
        size_names = size_qty.keys()
        print("contexts size_names", size_names)
        qty = size_qty.values()
        print("qty", qty)
        line_qty = int(sum(qty))
        print("line_qty", line_qty)
        line_total = line_qty * product.product_price
        print("line_total", line_total)
        # total += qty * product.product_price
        bag_items.append({
                            'item_id': item_id,
                            'product_type': str(product.product_type),
                            'size_qty': item_data,
                            'line_qty': line_qty,
                            'line_total': line_total,
                            'product': product,
                        })
        
        line_totals.append(line_total)

    print("line_totals", line_totals)
    grand_total = delivery + sum(line_totals)

    context = {
        'bag_items': bag_items,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
