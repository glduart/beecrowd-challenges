[init_hour, end_hour] = [int(x) for x in input().strip().split(" ")]

game_time = end_hour - init_hour

if game_time <= 0:
    game_time += 24

print(f"O JOGO DUROU {game_time} HORA(S)")