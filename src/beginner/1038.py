menu = (4, 4.5, 5, 2, 1.5)

order = input("").strip().split(" ")
[product_code, quantity] = [int(info) for info in order]
product = menu[product_code - 1]
print(f"Total: R$ {product * quantity:.2f}")