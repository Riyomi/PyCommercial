from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('', views.homePage, name='home'),
    path('browse', views.browsePage, name='browse'),
    path('browse/product/<int:product_id>',
         views.productDetailsPage, name='details'),
    path('checkout', views.checkoutPage, name='checkout'),
    path('add-to-cart', views.addToCart, name='add-to-cart'),
    path('remove-from-cart', views.removeFromCart, name='remove-from-cart'),
]
