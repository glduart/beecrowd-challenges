product1 = input("").strip().split(" ")
[product1_code, product1_units, product1_price_per_unit] = product1

product1_code = int(product1_code)
product1_units = int(product1_units)
product1_price_per_unit = float(product1_price_per_unit)

product2 = input("").strip().split(" ")
[product2_code, product2_units, product2_price_per_unit] = product2

product2code = int(product2_code)
product2_units = int(product2_units)
product2_price_per_unit = float(product2_price_per_unit)

amount = (product1_units * product1_price_per_unit) + (product2_units * product2_price_per_unit)

print(f"VALOR A PAGAR: R$ {amount:.2f}")

