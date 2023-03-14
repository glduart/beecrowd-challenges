all_test_cases_results = []
while True:
    monster_infos = input("").strip().split(" ")
    if monster_infos == ["0", "0"]:
        break
    [xp_increase_multiplier, monster_xp] = [int(x) for x in monster_infos]
    all_test_cases_results.append(monster_xp * xp_increase_multiplier)

for test_case_result in all_test_cases_results:
    print(test_case_result)