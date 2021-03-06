from django.shortcuts import render, get_object_or_404
from model_utils.managers import InheritanceManager
from django.contrib import messages
from django.db.models import Q
from .models import (Product, Category,
                     Type, Ring, Clothing)
from profiles.models import UserProfile


def collections(request):
    """
    A view to show all products / product collections
    """
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        user_categories = profile.categories
        permissions_list = user_categories[0:]
        products = Product.objects.filter(
            product_category__in=Category.objects.filter(
                name__in=permissions_list))
        categories = Category.objects.all()
        permissions_categories = Category.objects.filter(
                                            name__in=permissions_list)
        product_type = Type.name
        product_category = Category.name
        jewellery_size_type = Product.SizeType.jewellery_sizes
        ring = Ring.objects.all()
        clothing_sizes = Clothing(Product).ClothingSizes.choices
        chosen_categories = None

        if request.GET:  # filter the products by category checkbox
            chosen_categories = request.GET.getlist('chosen_categories')
            products = Product.objects.filter(
                            product_category__in=Category.objects.filter(
                                name__in=chosen_categories))

        context = {
            'profile': profile,
            'permissions_list': permissions_list,
            'products': products,
            'categories': categories,
            'product_category': str(product_category),
            'jewellery_size_type': jewellery_size_type,
            'ring': ring,
            'clothing_sizes': clothing_sizes,
            'categories': categories,
            'chosen_categories': chosen_categories,

        }
        return render(request, 'products/collections.html', context)
    return render(request, 'home/index.html')


def product_detail(request, product_id):
    """
    A view to show full detail of selected product
    """
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        product = get_object_or_404(Product, pk=product_id)
        user_categories = profile.categories
        permissions_list = user_categories[0:]
        categories = Category.name
        product_category = str(product.product_category)
        product_type = Type.name
        jewellery_size_type = Product.SizeType.jewellery_sizes
        ring = Ring.objects.all()
        clothing_sizes = Clothing(Product).ClothingSizes.choices

        context = {
            'profile': profile,
            'permissions_list': permissions_list,
            'product': product,
            'product_category': product_category,
            'categories': categories,
            'product_type': str(product_type),
            'jewellery_size_type': jewellery_size_type,
            'ring': ring,
            'clothing_sizes': clothing_sizes
        }
        return render(request, 'products/product_detail.html', context)
