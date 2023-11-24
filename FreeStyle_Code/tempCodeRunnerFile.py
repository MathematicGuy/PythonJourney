''' Replace items in n pos '''

zero = '0 0 0 0 0'
print('-> ', zero[1])

pos = 7
if pos % 2 == 0:
    follow_pos = pos + 1
    new_zero = zero[0:pos] + '2' + zero[follow_pos:]
    print(new_zero)
else:
    print('pls enter a new number')


