def are_multiples(dividend, divider):
    print("Sao Multiplos") if dividend % divider == 0 else print("Nao sao Multiplos")

[a, b] = [int(x) for x in input().strip().split(" ")]

if b > a:
    are_multiples(b, a)
else:
    are_multiples(a, b)