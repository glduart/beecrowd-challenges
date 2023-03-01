values = input("").strip().split(" ")

[a, b, c] = map(lambda x: float(x), values)

rectangled_triangle_area = a * c / 2
circle_area = c ** 2 * 3.14159
trapezium_area = (a + b) * c / 2
square_area = b ** 2
rectangle_area = a * b

print(f"TRIANGULO: {rectangled_triangle_area:.3f}")
print(f"CIRCULO: {circle_area:.3f}")
print(f"TRAPEZIO: {trapezium_area:.3f}")
print(f"QUADRADO: {square_area:.3f}")
print(f"RETANGULO: {rectangle_area:.3f}")