money = float(input())
money += 0.001 # Para contornar o problema de precisão do tipo float

available_notes = (
    {"name": "NOTA", 
     "available": [
        {"note": 100.00, "amount": 0},
        {"note": 50.00, "amount": 0},
        {"note": 20.00, "amount": 0},
        {"note": 10.00, "amount": 0},
        {"note": 5.00, "amount": 0},
        {"note": 2.00, "amount": 0}
    ]}, 
    {"name": "MOEDA", 
     "available": [
        {"note": 1.00, "amount": 0},
        {"note": 0.50, "amount": 0},
        {"note": 0.25, "amount": 0},
        {"note": 0.10, "amount": 0},
        {"note": 0.05, "amount": 0},
        {"note": 0.01, "amount": 0}
    ]}
)
while money >= 0.01:
    for cash in available_notes:
        for notes in cash["available"]:
            while money >= notes["note"]:
                notes["amount"] += 1 
                money = money -notes["note"]
                    
for cash in available_notes:
    print(f"{cash['name'] + 'S'}:")
    for notes in cash["available"]:
        print(f"{notes['amount']} {cash['name'].lower()}(s) de R$ {notes['note']:.2f}")