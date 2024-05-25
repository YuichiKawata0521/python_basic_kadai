def purchase_price(price, con_tax):
    total_price = price * (1 + con_tax / 100)

    return total_price

print(purchase_price(100, 10))
