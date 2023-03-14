positions = (1, 3, 5, 10, 25, 50, 100)
team_position = int(input(""))

for position in positions:
    if team_position <= position:
        print(f"Top {position}")
        break