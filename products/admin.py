from django.contrib import admin
from .models import Product, Category, Order, OrderItem, Review


class OrderItemInLine(admin.StackedInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer')
    inlines = [OrderItemInLine]


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


# Register your models here.

admin.site.register([Category, OrderItem, Review])
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
