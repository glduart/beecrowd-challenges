grades = [
    {"letter": "A", "numeric_interval": [86, 100]},
    {"letter": "B", "numeric_interval": [61,85]},
    {"letter": "C", "numeric_interval": [36, 60]}, 
    {"letter": "D", "numeric_interval": [1, 35]}
]

student_grade = int(input(""))

for grade in grades:
    if student_grade == 0:
        print("E")
        break
    if student_grade >= grade["numeric_interval"][0] and student_grade <= grade["numeric_interval"][1]:
        print(grade["letter"])
        break