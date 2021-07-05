from django.contrib import admin
from .models import Product, Category, Order, OrderItem, Review


class OrderItemInLine(admin.StackedInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer')
    inlines = [OrderItemInLine]


# Register your models here.
admin.site.register([Product, Category, OrderItem, Review])
admin.site.register(Order, OrderAdmin)
