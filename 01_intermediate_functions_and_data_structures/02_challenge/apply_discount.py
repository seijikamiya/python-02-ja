def apply_discount(products, minimum_price, discount_rate):
    return [(lambda n: (n['name'], n['price']*(1-discount_rate/100)))(product) for product in products if product["price"]>minimum_price]