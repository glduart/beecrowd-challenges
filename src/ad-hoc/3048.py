sequence_size = int(input(""))
marked_numbers = 0
sequence = []

for c in range(0, sequence_size):
    number = int(input(""))
    sequence.append(number)
    if c == 0:
        marked_numbers += 1
    else: 
        if number != sequence[c - 1]:
            marked_numbers += 1

print(marked_numbers)