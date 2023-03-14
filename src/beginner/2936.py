GUESTS_PORTION  = (300, 1500, 600, 1000, 150)
cassava = 225
for portion in GUESTS_PORTION:
    how_much = int(input(""))
    cassava += how_much * portion

print(cassava)