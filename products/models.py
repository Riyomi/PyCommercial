from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Product(models.Model):
    name = models.CharField('Product Name', max_length=100)
    image = models.ImageField(upload_to='products/static/images')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField('Description', blank=True, null=True)
    price = models.DecimalField('Price', max_digits=9, decimal_places=2)
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
    customer = models.ForeignKey('users.Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField('Quantity', default=1)

    def __str__(self):
        return self.id


# When working directly with the model, make sure to call the model full_clean method
# before saving the model in order to trigger the validators. This is not required
# when using ModelForm since the forms will do that automatically.
class Review(models.Model):
    customer = models.ForeignKey('users.Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    value = models.IntegerField(default=3, validators=[
                                MaxValueValidator(5), MinValueValidator(1)])
    comment = models.TextField('Description', blank=True, null=True)

    def __str__(self):
        return self.id
