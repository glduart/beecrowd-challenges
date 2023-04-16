test_cases = int(input())
for _ in range(test_cases):
    [str1, str2] = input().strip().split(" ")
    biggest = str1 if len(str1) > len(str2) else str2
    final_str = ""
    last_zip = 0
    for c1, c2 in zip(str1, str2):
        final_str += c1 + c2
        last_zip += 1
    final_str += biggest[last_zip:]
    print(final_str)