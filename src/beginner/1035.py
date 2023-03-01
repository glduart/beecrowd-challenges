numbers = input().strip().split(" ")
[a, b, c, d] = map(lambda x: int(x), numbers)

print("Valores aceitos" 
      if (b > c and d > a) and (c + d > a + b) and (c > 0 and d > 0) and (a%2==0) 
else "Valores nao aceitos") 