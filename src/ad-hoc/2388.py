distance = 0
intervals = int(input(""))
for c in range(0, intervals):
    infos = input("").strip().split(" ")
    [time, speed] = map(lambda x: int(x),infos)
    distance += time * speed

print(distance)
