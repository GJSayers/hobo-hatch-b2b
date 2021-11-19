from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    line_totals = []
    line_qtys = []
    print("line_totals", line_totals)
    bag = request.session.get('bag', {})
    total = 0
    total_items = 0
    delivery = Decimal(settings.STANDARD_DELIVERY_COST)

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        product_type = str(product.product_type)
        size_qty = item_data[product_type]
        size_items = size_qty.items()
        size_names = size_qty.keys()
        qty = size_qty.values()
        line_qty = int(sum(qty))
        line_total = line_qty * product.product_price
        
        print("total", total)
        # line_count = int(sum(line_qty))
        # product_count += line_count
        # total += int(sum(line_total))
        bag_items.append({
                                'item_id': item_id,
                                'product_type': str(product.product_type),
                                'qty': qty,
                                'size_items': size_items,
                                'size_names': size_names,
                                'line_qty': line_qty,
                                'line_total': line_total,
                                'total': total,
                                'product': product,
                            })

        line_totals.append(line_total)
        line_qtys.append(line_qty)
        total_items = sum(line_qtys)
        total = sum(line_totals)

    print("line_totals", line_totals)
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'delivery': delivery,
        'total': total,
        'total_items': total_items,
        'grand_total': grand_total,
    }

    return context
