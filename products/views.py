from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

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


def addToCart(request):
    cart = {}

    cart[request.GET['id']] = {
        'name': request.GET['name'],
        'img_url': request.GET['img_url'],
        'price': float(request.GET['price']),
        'quantity': int(request.GET['quantity']),
    }

    if 'cartdata' in request.session:
        cart_data = request.session['cartdata']
        if request.GET['id'] in request.session['cartdata']:
            cart_data[request.GET['id']
                      ]['quantity'] += int(request.GET['quantity'])
            cart_data.update(cart_data)
        else:
            cart_data.update(cart)
    else:
        request.session['cartdata'] = cart

    totalitems = 0
    for key, value in request.session['cartdata'].items():
        totalitems += value['quantity']

    request.session['totalitems'] = totalitems

    return JsonResponse({'data': request.session['cartdata'], 'totalitems': totalitems})
