test_cases = int(input())

for _ in range(test_cases):
    [n1, n2] = input().strip().split(" ")
    if n1[-(len(n2)):] == n2:
        print("encaixa")
    else:
        print("nao encaixa")