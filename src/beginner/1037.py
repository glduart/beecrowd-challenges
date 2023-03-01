number = float(input(""))

if number < 0 or number > 100:
    print("Fora de intervalo")
    quit()

intervals = [(0,25), (25,50), (50,75), (75,100)]
for index, interval in enumerate(intervals):
    if index == 0:
        if number >= interval[0] and number <= interval[1]:
            print(f"Intervalo [{interval[0]},{interval[1]}]")
    else:            
        if number > interval[0] and number <= interval[1]:
            print(f"Intervalo ({interval[0]},{interval[1]}]")