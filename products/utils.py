def refreshTotal(request):
    totalitems = 0
    totalprice = 0
    for key, value in request.session['cartdata'].items():
        totalitems += value['qty']
        totalprice += value['total']

    request.session['totalitems'] = totalitems
    request.session['totalprice'] = totalprice

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


def get_subcategories(category):
    result = [category]

    for child in category.get_children():
        if child not in result:
            result.append(child)
        if child.get_children().count():
            result.extend(child.get_children())

    return result
