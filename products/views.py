from django.shortcuts import render

from .models import Product


def homePage(request):
    return render(request, 'products/home.html')


def browsePage(request):
    products = Product.objects.all()
    return render(request, 'products/browse.html', context={'products': products})
