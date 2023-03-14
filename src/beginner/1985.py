products = [
    {"product_code": 1001, "price": 1.50},
    {"product_code": 1002, "price": 2.50},
    {"product_code": 1003, "price": 3.50},
    {"product_code": 1004, "price": 4.50},
    {"product_code": 1005, "price": 5.50}
]

purchased_amount = 0
purchased_products = int(input(""))
for c in range(0, purchased_products):
    product_infos = input("").strip().split(" ")
    [product_code, quantity] = [int(x) for x in product_infos]
    for product in products:
        if product["product_code"] == product_code:
            purchased_amount += product["price"] * quantity
print(f"{purchased_amount:.2f}")