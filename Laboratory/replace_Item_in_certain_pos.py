zero = '0 0 0 0 0'

print('len: ', len(zero))

for pos in range(0, len(zero)):
    print(pos)
    if pos % 2 == 0 and (pos + 1) < len(zero):
        follow_pos = pos + 1
        new_zero = zero[0:pos] + '1' + zero[follow_pos:]
        print(new_zero)
    else:
        print('pls enter a new number')
    print('---------------------------------')
