from django.shortcuts import render
from .models import (Product, ProductCategory,
                    ProductType, Ring) # JewelleryProperties


def collections(request):
    """
    A view to show all products / product collections
    """
    
    products = Product.objects.all()
    categories = ProductCategory()
    product_type = ProductType()
    # rings = Ring.objects.all()
    # ring_sizes = JewelleryProperties.RingSizes

    context = {
        'products': products,
        'categories': categories,
        'product_type': product_type,
        # 'rings': rings,
        # 'ring_sizes': ring_sizes,
    }
    return render(request, 'products/collections.html', context)
