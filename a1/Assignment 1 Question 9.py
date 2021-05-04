import math

def cad_cashier(price, payment):
    price = round(price/5,2)*5
    return round(payment-price,2)


