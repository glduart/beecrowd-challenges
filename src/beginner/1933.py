cards = input("").strip().split(" ")
[card_1, card_2] = [int(card) for card in cards] 

if card_1 == card_2 or card_1 > card_2:
    print(card_1)
else:
    print(card_2)