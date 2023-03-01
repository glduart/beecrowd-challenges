from math import sqrt

numbers = input("").strip().split(" ")
[a, b ,c] = map(lambda x:float(x), numbers)

delta = b**2 - 4*a*c
 
try:
    result1 = (-b + sqrt(delta)) / (2 * a)
    result2 = (-b - sqrt(delta)) / (2 * a)
except (ZeroDivisionError, ValueError):
    print("Impossivel calcular")
    quit()

print(f"R1 = {result1:.5f}\nR2 = {result2:.5f}")