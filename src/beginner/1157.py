number = int(input(""))
for c in range(1, number):
    if number % c == 0:
        print(c)
print(number)