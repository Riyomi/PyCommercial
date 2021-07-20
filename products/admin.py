from django.contrib import admin
from .models import Product, Category, Order, OrderItem, Review


class OrderItemInLine(admin.StackedInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer')
    exclude = ('payment',)
    readonly_fields = ['creditcard', ]

    inlines = [OrderItemInLine]

    def creditcard(self, order):
        return '{}\n{}\n{}\n'.format(order.payment.name, order.payment.number, order.payment.expiry_date)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


# Register your models here.

admin.site.register([Category, OrderItem, Review])
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
