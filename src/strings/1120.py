all_test_cases = []

while True:
    [failed_digit, originally_contract] = input("").strip().split(" ")
    if failed_digit == "0" and originally_contract == "0":
        break
    if failed_digit not in originally_contract:
        all_test_cases.append(int(originally_contract))
        continue

    originally_contract = list(originally_contract)
    real_contract = []

    for letter in originally_contract:
        if letter != failed_digit:
            real_contract.append(letter)
    real_contract = int("".join(real_contract)) if len(real_contract) > 0  else 0

    all_test_cases.append(real_contract)

for case in all_test_cases:
    print(case)