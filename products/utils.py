def totalItemsAndPrice(data):
    totalitems = 0
    totalprice = 0
    for key, value in data.items():
        totalitems += value['qty']
        totalprice += value['total']

    return (totalitems, totalprice)
