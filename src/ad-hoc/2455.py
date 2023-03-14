infos = input("").strip().split(" ")
[p1, c1, p2, c2] = [int(x) for x in infos]

if p1 * c1 == p2 * c2:
    print(0)
elif p1 * c1 > p2 * c2:
    print(-1)
else:
    print(1)