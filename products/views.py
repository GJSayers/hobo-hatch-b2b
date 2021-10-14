from django.shortcuts import render
from model_utils.managers import InheritanceManager
from .models import (Product, ProductCategory,
                     ProductType, Ring, Clothing)  # JewelleryProperties


def collections(request):
    """
    A view to show all products / product collections
    """
    
    products = Product.objects.all()
    categories = ProductCategory.name
    product_type = ProductType.name
    jewellery_size_type = Product.SizeType.jewellery_sizes
    ring = Ring.objects.all()
    clothing_sizes = Clothing(Product).ClothingSizes.choices
    print(jewellery_size_type)
    print(ring)
    
    context = {
        'products': products,
        'categories': categories,
        'product_type': product_type,
        'jewellery_size_type': jewellery_size_type,
        'ring': ring,
        'clothing_sizes': clothing_sizes
    }
    return render(request, 'products/collections.html', context)
