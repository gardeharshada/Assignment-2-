# WAP to calculate the selling price of a book based on cost price and discount:
def selling_price(cost_price, discount):
    return cost_price - (cost_price * discount / 100)
cost_price = 100
discount = 20
print("selling price:", selling_price(cost_price, discount))