def calculate_discount (price,discount_percent):
    if discount_percent > 20 :
        numerator= price *discount_percent
        discount =numerator/100
        final_price= price -discount
        return final_price
    else:
        return price 

price = int(input('enter price'))
discount_percent = int(input('enter discount'))

print(calculate_discount(price,discount_percent))

