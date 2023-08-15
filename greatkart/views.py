from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import Products
from category.models import Category


def home(request):
    products = Products.objects.all().filter(is_available = True)
    category = Category.objects.all()

    context = {
        'Products':products,
        'Category':category,
        
    }
    return render(request,"home.html",context)