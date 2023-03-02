number_of_test_cases = int(input(""))
all_messages = []
for x in range(0, number_of_test_cases):
    message_to_encypt = input("").strip()
    message_to_encypt = list(message_to_encypt)
    for index, letter in enumerate(message_to_encypt):
        letter_in_ascii = ord(letter)
        if (letter_in_ascii >= 65 and letter_in_ascii <= 90) or (letter_in_ascii >= 97 and letter_in_ascii <= 122):
            letter_in_ascii += 3
            message_to_encypt[index] = chr(letter_in_ascii)
    message_to_encypt.reverse()
    for index, letter in enumerate(message_to_encypt):
        if index >= len(message_to_encypt) // 2:
            letter_in_ascii = ord(letter)
            letter_in_ascii -= 1
            message_to_encypt[index] = chr(letter_in_ascii)
    message_to_encypt = ''.join(message_to_encypt)
    all_messages.append(message_to_encypt)
for message in all_messages:
    print(message)