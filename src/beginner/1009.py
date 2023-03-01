sellers_name = input("")
fixed_salary = float(input(""))
sold_in_month = float(input(""))

commission = sold_in_month * 15 / 100

print(f"TOTAL = R$ {fixed_salary + commission:.2f}")