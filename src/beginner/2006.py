tea_type = int(input(""))
contestants_answers = input("").strip().split(" ")
contestants_answers = list(map(lambda x: int(x), contestants_answers))

right_answers = 0
for answer in contestants_answers:
    if answer == tea_type:
        right_answers += 1
print(right_answers)