values = input("").strip().split(" ")

[a, b, c] = map(lambda x: float(x), values)


greatestAB = (a + b + abs(a - b)) / 2
greatestBC = (b + c + abs(b - c)) / 2

greatest = (greatestAB + greatestBC + abs(greatestAB - greatestBC)) / 2

print(f"{greatest:.0f} eh o maior")
