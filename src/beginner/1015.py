from math import sqrt

p1 = input("").strip().split(" ")
[p1x, p1y] = map(lambda x: float(x), p1)

p2 = input("").strip().split(" ")
[p2x, p2y] = map(lambda x: float(x), p2)

distance = sqrt((p2x - p1x)**2 + (p2y - p1y)**2)


print(f"{distance:.4f}")