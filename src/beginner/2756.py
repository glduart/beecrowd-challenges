letters = ["A", "B", "C", "D", "E"]
space_between_letters_number = 1
space_around_number = 7

for letter in letters:
    space_around = " " * space_around_number
    print(space_around, end="")
    if letter == "A":
        print(letter)
    else:
        print(letter + " " * space_between_letters_number+ letter)
        space_between_letters_number += 2
    space_around_number -= 1

space_between_letters_number = 5
space_around_number = 4
letters.pop()
letters = letters[::-1]

for letter in letters: 
    space_around = " " * space_around_number
    print(space_around, end="")
    if letter == "A":
        print(letter)
    else:
        print(letter + " " * space_between_letters_number + letter)
        space_between_letters_number -= 2
    space_around_number += 1



# De uma forma mais direta :)
""" 
print('       A')
print('      B B')
print('     C   C')
print('    D     D')
print('   E       E')
print('    D     D')
print('     C   C')
print('      B B')
print('       A') 
"""