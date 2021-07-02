def totalItemsAndPrice(data):
    totalitems = 0
    totalprice = 0
    for key, value in data.items():
        totalitems += value['qty']
        totalprice += (value['price']*value['qty'])

    return (totalitems, totalprice)
