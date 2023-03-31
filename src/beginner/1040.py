numbers = input("").strip().split(" ")
[n1, n2, n3, n4] = [float(x) for x in numbers]
average = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10
print(f"Media: {average:.1f}")
if average >= 7:
    print("Aluno aprovado.")
elif average < 5:
    print("Aluno reprovado.")
else: 
    print("Aluno em exame.")
    exam_score = float(input(""))
    final_average = (average + exam_score) / 2
    print(f"Nota do exame: {exam_score:.1f}")
    print("Aluno aprovado." if final_average >= 5 else "Aluno reprovado.")
    print(f"Media final: {final_average:.1f}")