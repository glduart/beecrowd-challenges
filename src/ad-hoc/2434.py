infos = input("").strip().split(" ")
[days, balance] = [int(x) for x in infos]
lowest_balance_amount = balance
for x in range(1, days + 1):
    account_movement = int(input(""))
    if account_movement > 0:
        balance += account_movement
    else:
        balance += account_movement
        if balance < lowest_balance_amount:
            lowest_balance_amount = balance
print(lowest_balance_amount)