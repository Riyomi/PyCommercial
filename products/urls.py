from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('', views.homePage, name='home'),
    path('browse', views.browsePage, name='browse'),
    path('browse/product/<int:product_id>/',
         views.productDescriptionPage, name="details"),
    path('browse/product/<int:product_id>/details',
         views.productDescriptionPage, name="product-description"),
    path('browse/product/<int:product_id>/reviews',
         views.productReviewsPage, name="product-reviews"),
    path('checkout', views.checkoutPage, name='checkout'),
    path('add-to-cart', views.addToCart, name='add-to-cart'),
    path('remove-from-cart', views.removeFromCart, name='remove-from-cart'),
    path('place-order', views.placeOrder, name='place-order'),
    path('rate-product', views.rateProduct, name="rate-product"),
]
