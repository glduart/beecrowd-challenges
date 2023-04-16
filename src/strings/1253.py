def caesar_cipher(sentence):
    alphabet = [chr(ascii_code) for ascii_code in range(65, 91)]
    encoded_sentence = ""
    for letter in sentence:
        letter_in_alphabet = alphabet.index(letter)
        encoded_sentence += alphabet[(letter_in_alphabet - shift)  % 26]
    return encoded_sentence


test_cases = int(input())

for _ in range(test_cases):
    sentence = list(input())
    shift = int(input())
    encoded_sentence = caesar_cipher(sentence)
    print(encoded_sentence)
