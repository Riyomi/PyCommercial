from .models import Product, Category


def totalItemsAndPrice(data):
    totalitems = 0
    totalprice = 0
    for key, value in data.items():
        totalitems += value['qty']
        totalprice += value['total']

    return (totalitems, totalprice)


def get_all_categories(product):
    path = [product.name]
    current = product.category
    while True:
        path.append(current.name)
        current = current.parent
        if current is None:
            path.append('Products')
            break
    return path
