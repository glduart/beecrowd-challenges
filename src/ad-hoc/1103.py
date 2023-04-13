while True:
    [h1, m1, h2, m2] = [int(x) for x in input().strip().split(" ")]
    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break
    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2
    t2 += 24 * 60 if t2 < t1 else 0
    print(t2 - t1)