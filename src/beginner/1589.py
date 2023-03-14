tests_cases = int(input(""))
all_test_cases_results = []

for c in range(0, tests_cases):
    radii = input("").strip().split(" ")
    [r1, r2] = [int(x) for x in radii]
    all_test_cases_results.append(r1 + r2)

for test_case_result in all_test_cases_results:
    print(test_case_result)