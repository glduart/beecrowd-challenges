numbers = input("").strip().split(" ")
numbers = [int(x) for x in numbers]
ascending_numbers = sorted(numbers)

for ascending in ascending_numbers:
    print(ascending)
print()
for number in numbers:
    print(number)