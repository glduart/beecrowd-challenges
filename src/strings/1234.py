all_test_cases_results = []
while True:
    try:
        sentence = list(input(""))
    except EOFError:
        break
    if sentence == []:
         break
    turn_uppercase = True
    for index, letter in enumerate(sentence): 
        ascii_code = ord(letter)
        if (ascii_code >= 65 and ascii_code <= 90) or (ascii_code >= 97 and ascii_code <= 122):
            if turn_uppercase:
                sentence[index] = letter.upper()
                turn_uppercase = False
            else:
                sentence[index] = letter.lower()
                turn_uppercase = True
    all_test_cases_results.append(sentence)

for test_case in all_test_cases_results:
    print(''.join(test_case))