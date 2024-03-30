def calculate_discount(price,discount_percent):
    if discount_percent >=20:
     discount= discount_percent/100 * price
     final_price = price - discount
    else:
       final_price = price
    return final_price


price = int(input("Enter original price"))
discount_percent = float(input("Enter discount percent"))
final_price = calculate_discount(price,discount_percent)
print(f"The final price after {discount_percent:.2f}% discount is: ${final_price:.2f}")