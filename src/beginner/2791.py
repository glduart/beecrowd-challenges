cups = input("").strip().split(" ")
for index, cup in enumerate(cups):
    if cup == "1":
        print(index + 1)