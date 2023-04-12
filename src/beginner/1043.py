values = input("").strip().split(" ")
[a, b, c] = [float(x) for x in values]
if c > abs(a - b) and c < a + b:
    print(f"Perimetro = {a + b + c:.1f}")
else:
    print(f"Area = {((a + b) * c) / 2:.1f}")