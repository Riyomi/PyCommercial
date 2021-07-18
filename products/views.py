from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator

from .forms import CustomerInfoOrderForm, UserInfoOrderForm
from .models import Product, Order, OrderItem, Review, Category
from .utils import totalItemsAndPrice, get_all_categories, get_subcategories
from django.db.models import Avg


def homePage(request):
    main_categories = Category.objects.filter(
        parent=None).order_by('-id')

    best_products = Product.objects.annotate(
        avg_rating=Avg('review__value')).order_by('-avg_rating')[:5]

    data = {}

    for category in main_categories:
        data[category] = get_subcategories(category)

    recommendations = []

    # Get the first 5 products ordered by average rating, from the first 3 main categories
    for category in main_categories[:3]:
        recommendations.append([
            get_subcategories(category),
            Product.objects.annotate(
                avg_rating=Avg('review__value')).order_by('-avg_rating').filter(category__in=get_subcategories(category))[:5]
        ])

    return render(request, 'products/home.html', {'data': data, 'best_products': best_products, 'recommendations': recommendations})


def browsePage(request):
    search_param = request.GET.get('search', '')

    max_price = Product.objects.latest('price').price

    max_price_filter = request.GET.get('maxPrice') if request.GET.get(
        'maxPrice') else max_price

    main_categories = Category.objects.filter(parent=None).order_by('name')

    category_filters = []

    for param in request.GET:
        if param != 'search' and param != 'maxPrice' and param != 'page':
            category_filters.append(param)

    query_string = request.get_full_path(
    ) if request.get_full_path().find('?') != -1 else ''

    if query_string.find('page') >= 0:
        query_string = query_string[query_string.find('&')+1:]
    else:
        query_string = query_string[query_string.find('?')+1:]

    products = Product.objects.filter(
        name__contains=search_param, price__lte=max_price_filter, category__name__in=category_filters).order_by('id') if len(category_filters) > 0 else Product.objects.filter(
        name__contains=search_param, price__lte=max_price_filter).order_by('id')

    ratings = []

    paginator = Paginator(products, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products/browse.html', {'page_obj': page_obj, 'main_categories': main_categories, 'max_price': max_price, 'query_string': query_string})


def productDescriptionPage(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    categories = get_all_categories(product)
    reviews = Review.objects.filter(product=product)

    return render(request, 'products/productDetails/descriptionPage.html', {'product': product, 'categories': categories, 'reviews': reviews})


def productReviewsPage(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    categories = get_all_categories(product)
    reviews = Review.objects.filter(product=product)

    return render(request, 'products/productDetails/reviewsPage.html', {'product': product, 'categories': categories, 'reviews': reviews})


def checkoutPage(request):
    if request.POST:
        if request.method == 'POST':
            user_info_order_form = UserInfoOrderForm(
                request.POST)
            customer_info_order_form = CustomerInfoOrderForm(
                request.POST)

            if user_info_order_form.is_valid() and customer_info_order_form.is_valid():
                pass

    elif request.user.is_authenticated:
        user_info_order_form = UserInfoOrderForm(instance=request.user)
        customer_info_order_form = CustomerInfoOrderForm(
            instance=request.user.customer)
    else:
        user_info_order_form = UserInfoOrderForm()
        customer_info_order_form = CustomerInfoOrderForm()

    setplaceholders(user_info_order_form)
    setplaceholders(customer_info_order_form)

    customer_info_order_form.fields['mobile'].widget.attrs['placeholder'] = 'Mobile number'

    return render(request, 'products/checkout.html', {'user_info_order_form': user_info_order_form, 'customer_info_order_form': customer_info_order_form})


def addToCart(request):
    cart = {}

    cart[request.GET['id']] = {
        'name': request.GET['name'],
        'img_url': request.GET['img_url'],
        'price': int(request.GET['price']),
        'qty': int(request.GET['qty']),
        'total': int(request.GET['price'])*int(request.GET['qty']),
    }

    if 'cartdata' in request.session:
        cart_data = request.session['cartdata']
        if request.GET['id'] in request.session['cartdata']:
            cart_data[request.GET['id']
                      ]['qty'] += int(request.GET['qty'])
            cart_data[request.GET['id']
                      ]['total'] += int(request.GET['price'])*int(request.GET['qty'])
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
        return redirect('products:home')

    # TODO: redirect if it's empty (or just simply don't display the button in the HTML...)


def rateProduct(request):
    rating = int(request.POST['rating'])
    comment = request.POST['comment']
    product = Product.objects.get(pk=int(request.POST['product-id']))

    review = Review(customer=request.user.customer,
                    product=product, value=rating, comment=comment)
    review.save()

    return HttpResponseRedirect(reverse('products:product-reviews', args=(int(request.POST['product-id']),)))


def setplaceholders(form):
    for field in form.fields:
        form.fields[field].widget.attrs['placeholder'] = form.fields[field].label
