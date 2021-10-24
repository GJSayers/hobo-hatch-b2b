from django.shortcuts import render, get_object_or_404
from model_utils.managers import InheritanceManager
from django.contrib import messages
from django.db.models import Q
from .models import (Product, Category,
                     Type, Ring, Clothing)  # JewelleryProperties


def collections(request):
    """
    A view to show all products / product collections
    """
    
    products = Product.objects.all()
    categories = Category.objects.all()
    product_type = Type.name
    jewellery_size_type = Product.SizeType.jewellery_sizes
    ring = Ring.objects.all()
    clothing_sizes = Clothing(Product).ClothingSizes.choices
    chosen_categories = None

    if request.GET:
        chosen_categories = request.GET.getlist('chosen_categories')
        products = Product.objects.filter(product_category__in=Category.objects.filter(
                                          name__in=chosen_categories))

    context = {
        'products': products,
        'categories': categories,
        'product_type': product_type,
        'jewellery_size_type': jewellery_size_type,
        'ring': ring,
        'clothing_sizes': clothing_sizes,
        'categories': categories,
        'chosen_categories': chosen_categories,
    }
    return render(request, 'products/collections.html', context)


def product_detail(request, product_id):
    """
    A view to show full detail of selected product
    """
    
    product = get_object_or_404(Product, pk=product_id)
    categories = Category.name
    product_type = Type.name
    jewellery_size_type = Product.SizeType.jewellery_sizes
    ring = Ring.objects.all()
    clothing_sizes = Clothing(Product).ClothingSizes.choices
    
    
    context = {
        'product': product,
        'categories': categories,
        'product_type': product_type,
        'jewellery_size_type': jewellery_size_type,
        'ring': ring,
        'clothing_sizes': clothing_sizes
    }
    return render(request, 'products/collections.html', context)
