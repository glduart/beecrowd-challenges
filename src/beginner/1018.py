value = int(input(""))
value_counter = value

available_notes = (
    {"note": 100, "amount": 0, "str": "100,00"},
    {"note": 50, "amount": 0, "str": "50,00"},
    {"note": 20, "amount": 0, "str": "20,00"},
    {"note": 10, "amount": 0, "str": "10,00"},
    {"note": 5, "amount": 0, "str": "5,00"},
    {"note": 2, "amount": 0, "str": "2,00"},
    {"note": 1, "amount": 0, "str": "1,00"}
)

while value_counter != 0:
    for note in available_notes:
        while value_counter >= note["note"]:
            value_counter -= note["note"]
            note["amount"] += 1

print(value)
for note in available_notes:
    print(f"{note['amount']} nota(s) de R$ {note['str']}")