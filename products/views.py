from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.core.paginator import Paginator

from .forms import OrderForm
from .models import Product, Order, OrderItem, Review, Category, CreditCard
from .utils import refreshTotal, get_all_categories, get_subcategories, get_query_string
from django.db.models import Avg


def homePage(request):
    main_categories = Category.objects.filter(
        parent=None).order_by('-id')

    best_products = Product.objects.annotate(
        avg_rating=Avg('review__value')).order_by('-avg_rating')[:5]

    data = {}
    recommendations = []

    # From the first 3 main categories, get the first 5 products ordered by average rating,
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
        if param not in ['search', 'maxPrice', 'page']:
            category_filters.append(param)

    query_string = get_query_string(request)

    products = Product.objects.filter(
        name__contains=search_param, price__lte=max_price_filter, category__name__in=category_filters).order_by('id') if category_filters else Product.objects.filter(
        name__contains=search_param, price__lte=max_price_filter).order_by('id')

    paginator = Paginator(products, 8)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'products/browse.html', {'page': page, 'main_categories': main_categories, 'max_price': max_price, 'query_string': query_string})


def detailsPage(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    categories = get_all_categories(product)

    return render(request, 'products/details.html', {'product': product, 'categories': categories})


def checkoutPage(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            data = order_form.cleaned_data

            payment = CreditCard(
                name=data['name'], number=data['number'], expiry_date=data['expiry_date'])
            payment.save()

            customer = request.user.customer if request.user.is_authenticated else None
            order = Order(
                customer=customer,
                total=request.session['totalprice'],
                payment=payment,
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                mobile=data['mobile'],
                country=data['country'],
                city=data['city'],
                address=data['address'])

            order.save()

            for product_id, data in request.session['cartdata'].items():
                product = Product.objects.get(pk=product_id)
                qty = int(data['qty'])
                OrderItem.objects.create(
                    product=product, order=order, quantity=qty)

            del request.session['cartdata']
            del request.session['totalitems']
            del request.session['totalprice']

            if not request.user.is_authenticated:
                request.session['guest'] = order.id

            return redirect(reverse('users:order-details', kwargs={"order_id": order.id}))

    elif request.user.is_authenticated:
        order_form = OrderForm(instance=request.user.customer)
        order_form.fields['first_name'].initial = request.user.first_name
        order_form.fields['last_name'].initial = request.user.last_name
        order_form.fields['email'].initial = request.user.email

    else:
        order_form = OrderForm()

    order_form.fields['mobile'].widget.attrs['placeholder'] = 'Mobile number'

    return render(request, 'products/checkout.html', {'order_form': order_form})


def addToCart(request):
    cart = {}

    id = request.GET['id']

    product = Product.objects.get(pk=id)

    if product:
        cart[id] = {
            'name': product.name,
            'img_url': product.image.url.replace('/products', ''),
            'price': product.price,
            'qty': int(request.GET['qty']),
            'total': product.price * int(request.GET['qty']),
        }

        if 'cartdata' in request.session:
            cart_data = request.session['cartdata']
            if id in cart_data:
                cart_data[id]['qty'] += int(request.GET['qty'])
                cart_data[id]['total'] += product.price * \
                    int(request.GET['qty'])
                cart_data.update(cart_data)
            else:
                cart_data.update(cart)
        else:
            request.session['cartdata'] = cart

        refreshTotal(request)

        return JsonResponse({'data': request.session['cartdata'], 'totalitems': request.session['totalitems'], 'totalprice': request.session['totalprice']})

    return JsonResponse()


def removeFromCart(request):
    id = request.GET['id']

    if id in request.session['cartdata']:
        del request.session['cartdata'][id]

    refreshTotal(request)

    return JsonResponse({'data': request.session['cartdata'], 'totalitems': request.session['totalitems'], 'totalprice': request.session['totalprice']})


def rateProduct(request):
    rating = int(request.POST['rating'])
    comment = request.POST['comment']
    product = Product.objects.get(pk=int(request.POST['product-id']))

    review = Review(customer=request.user.customer,
                    product=product, value=rating, comment=comment)
    review.save()

    return redirect("%s?p=reviews" % reverse('products:details', kwargs={"product_id": int(request.POST['product-id'])}))
