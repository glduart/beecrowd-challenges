number_of_test_cases = int(input(""))
number_of_leds_of_all_test_cases = []
leds = [
    {"number": 1, "leds_amount": 2},
    {"number": 2, "leds_amount": 5},
    {"number": 3, "leds_amount": 5},
    {"number": 4, "leds_amount": 4},
    {"number": 5, "leds_amount": 5},
    {"number": 6, "leds_amount": 6},
    {"number": 7, "leds_amount": 3},
    {"number": 8, "leds_amount": 7},
    {"number": 9, "leds_amount": 6},
    {"number": 0, "leds_amount": 6}
]

for x in range(0, number_of_test_cases):
    leds_amount = 0
    number_leds = input("").strip()
    for number in number_leds:
        for led in leds:
            if int(number) == led["number"]:
                leds_amount += led["leds_amount"]
    number_of_leds_of_all_test_cases.append(leds_amount)

for leds_number in number_of_leds_of_all_test_cases:
    print(f"{leds_number} leds")
