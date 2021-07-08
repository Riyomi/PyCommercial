from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


class Product(models.Model):
    name = models.CharField('Product Name', max_length=100)
    image = models.ImageField(upload_to='products/static/images')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField('Description', blank=True, null=True)
    price = models.PositiveIntegerField('Price')
    stock = models.SmallIntegerField('Stock')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('Category Name', max_length=50)
    parent = models.ForeignKey(
        'Category', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    class Status(models.IntegerChoices):
        PLACED = 0
        PROCESSING = 1
        SHIPPED = 2
        DELIVERED = 3

    customer = models.ForeignKey(
        'users.Customer', on_delete=models.CASCADE, blank=True, null=True)
    total = models.PositiveIntegerField('Total', default=0)
    date_placed = models.DateTimeField('date placed', default=timezone.now)
    status = models.IntegerField(choices=Status.choices, default=Status.PLACED)

    def get_status_choices(self):
        return self.Status.choices

    def get_status_text(self):
        if self.status == self.Status.PLACED:
            return 'Placed'
        elif self.status == self.Status.PROCESSING:
            return 'Processing'
        elif self.status == self.Status.SHIPPED:
            return 'Shipped'
        else:
            return 'Delivered'

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    order = models.ForeignKey('products.Order', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        'Quantity', default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return str(self.id)


class Review(models.Model):
    customer = models.ForeignKey('users.Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    value = models.IntegerField(default=3, validators=[
                                MaxValueValidator(5), MinValueValidator(1)])
    comment = models.TextField('Description', blank=True, null=True)

    def __str__(self):
        return str(self.id)
