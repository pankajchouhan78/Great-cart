from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from store.models import Products
from category.models import Category
# Create your views here.

def store(request, category_slug = None):
    products = None
    category = None

    if category_slug:
        category = get_object_or_404(Category , slug = category_slug)
        products = Products.objects.filter(category = category, is_available = True)
        products_count = products.count()
    else:
        products = Products.objects.all().filter(is_available = True)
        products_count = products.count()
    
    context = {
        'Products': products,
        'product_count':products_count,
    }
    return render(request,"store/store.html",context)

def product_details(request, category_slug, product_slug):
    try:
        single_product = Products.objects.get(category__slug = category_slug, slug = product_slug)
    except Exception as e:
        return e
    
    context = {
        'single_products':single_product,
    }
    return render(request,"store/product_details.html", context)