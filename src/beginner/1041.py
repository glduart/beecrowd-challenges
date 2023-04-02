coordinates = input("").strip("").split(" ")
[x, y] = [float(coord) for coord in coordinates]
if x == 0 and y == 0:
    print("Origem")
elif x == 0: 
    print("Eixo X")
elif y == 0:
    (print("Eixo Y"))
else:
    if x > 0 and y > 0:
        print("Q1")
    elif x < 0 and y > 0:
        print("Q2")
    elif x  < 0 and y < 0:
        print("Q3")
    else:
        print("Q4")