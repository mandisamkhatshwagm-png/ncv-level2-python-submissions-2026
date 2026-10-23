def place_order(item):
    print(f"order place:your order is {item}")
    
def calculate_total(item):
    base_price = 25.5
    VAT = 0.15
    totalPrice = (base_price + len(item))*1.5
    return totalPrice
    
def get_order():
    print("preparing order...")
    return"collect your order"

myfood = input("what would you like")
place_order(myfood)

print(get_order())

order_total = calculate_total(myfood)
print(F"your order costs: {order_total}")

msg = get_order()