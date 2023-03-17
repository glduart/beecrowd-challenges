infos = input("").strip().split(" ")
[initial_hour, initial_minute, ended_hour, ended_minute] = [int(x) for x in infos]


initial_time_in_minutes = (initial_hour * 60) + initial_minute
ended_time_in_minutes = (ended_hour * 60) + ended_minute
time_difference = ended_time_in_minutes - initial_time_in_minutes

if time_difference <= 0:
    time_difference += 24*60
hours = time_difference // 60
minutes = time_difference - (hours * 60)
print(f"O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)")