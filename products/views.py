from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import Avg

from .models import Product, Order, OrderItem, Review
from .utils import totalItemsAndPrice, get_all_categories


def homePage(request):
    return render(request, 'products/home.html')


def browsePage(request):
    search_param = request.GET.get('search')

    products = Product.objects.get_queryset().order_by('id')

    if search_param:
        products = Product.objects.filter(name__contains=search_param)

    paginator = Paginator(products, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products/browse.html', {'page_obj': page_obj})


def productDescriptionPage(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    categories = get_all_categories(product)

    reviews = Review.objects.filter(product=product)

    avg_stars = reviews.aggregate(Avg('value'))['value__avg']

    return render(request, 'products/productDetails/descriptionPage.html', {'product': product, 'categories': categories, 'reviews': reviews, 'avg_stars': avg_stars})


def productReviewsPage(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    categories = get_all_categories(product)
    reviews = Review.objects.filter(product=product)

    avg_stars = reviews.aggregate(Avg('value'))['value__avg']

    return render(request, 'products/productDetails/reviewsPage.html', {'product': product, 'categories': categories, 'reviews': reviews, 'avg_stars': avg_stars})


def checkoutPage(request):
    return render(request, 'products/checkout.html')


def addToCart(request):
    cart = {}

    cart[request.GET['id']] = {
        'name': request.GET['name'],
        'img_url': request.GET['img_url'],
        'price': float(request.GET['price']),
        'qty': int(request.GET['qty']),
        'total': float(request.GET['price'])*int(request.GET['qty']),
    }

    if 'cartdata' in request.session:
        cart_data = request.session['cartdata']
        if request.GET['id'] in request.session['cartdata']:
            cart_data[request.GET['id']
                      ]['qty'] += int(request.GET['qty'])
            cart_data[request.GET['id']
                      ]['total'] += float(request.GET['price'])*int(request.GET['qty'])
            cart_data.update(cart_data)
        else:
            cart_data.update(cart)
    else:
        request.session['cartdata'] = cart

    totalitems, totalprice = totalItemsAndPrice(request.session['cartdata'])

    request.session['totalitems'] = totalitems
    request.session['totalprice'] = totalprice

    return JsonResponse({'data': request.session['cartdata'], 'totalitems': totalitems, 'totalprice': totalprice})


def removeFromCart(request):
    id = request.GET['id']
    if id in request.session['cartdata']:
        del request.session['cartdata'][id]

    totalitems, totalprice = totalItemsAndPrice(request.session['cartdata'])

    request.session['totalitems'] = totalitems
    request.session['totalprice'] = totalprice

    return JsonResponse({'data': request.session['cartdata'], 'totalitems': totalitems, 'totalprice': totalprice})


def placeOrder(request):
    if request.session['cartdata']:
        order = Order(
            customer=request.user.customer if request.user.is_authenticated else None, total=request.session['totalprice'])
        order.save()

        for product_id, data in request.session['cartdata'].items():
            product = Product.objects.get(pk=product_id)
            qty = int(data['qty'])
            OrderItem.objects.create(
                product=product, order=order, quantity=qty)

        del request.session['cartdata']
        del request.session['totalitems']
        del request.session['totalprice']
        return render(request, 'products/home.html')

    # TODO: redirect if it's empty (or just simply don't display the button in the HTML...)


def rateProduct(request):
    rating = int(request.POST['rating'])
    comment = request.POST['comment']
    product = Product.objects.get(pk=int(request.POST['product-id']))

    review = Review(customer=request.user.customer,
                    product=product, value=rating, comment=comment)
    review.save()

    return HttpResponseRedirect(reverse('products:product-reviews', args=(int(request.POST['product-id']),)))
