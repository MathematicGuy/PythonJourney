number = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
number_length = len(number)
print(number)
print('list len:',number_length)

for i in range(number_length):
    number[i] = 3
start = 0


for border in range(number_length):
    number[border] = border
    print(number)
    for start_pos in range(border, number_length):
        number[start_pos] = start_pos
        print(number)
    print()