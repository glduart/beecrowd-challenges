infos = input("").strip().split(" ")
[tabs_opened, number_of_actions] = map(lambda x: int(x), infos)
for c in range(0 , number_of_actions):
    action = input("").strip().lower()
    if action == "fechou":
        tabs_opened += 1
    else:
        tabs_opened -= 1
print(tabs_opened)