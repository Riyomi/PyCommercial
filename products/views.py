from django.shortcuts import render, get_object_or_404

from .models import Product


def homePage(request):
    return render(request, 'products/home.html')


def browsePage(request):
    search_param = request.GET.get('search')
    if search_param:
        products = Product.objects.filter(name__contains=search_param)
    else:
        products = Product.objects.all()
    return render(request, 'products/browse.html', {'products': products})


def productDetailsPage(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/details.html', {'product': product})
