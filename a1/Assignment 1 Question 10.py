import math

def cad_cashier(price, payment):
    price = round(price/5,2)*5
    return round(payment-price,2)
    
def min_CAD_coins(price, payment):
    '''(number, number) -> number, number, number, number, number
    Preconditions: "price" is a postive float no more than two decimal places and "price" is less than or equal to "payment"
    Returns the coins needed to give customer the change owed'''

    change = cad_cashier(price,payment)
    t = int(change//2)
    l = int(round((change - (t*2)),2)/1)
    q = int((round((change - (t*2) - l),2)/0.25))
    d = int((round((change - (t*2) - l - (q*0.25)),2)/0.1))
    n = int(round(change - (t*2) - l - (q*0.25) - (d*0.1),2)/0.05)
    return (t, l, q, d, n)
