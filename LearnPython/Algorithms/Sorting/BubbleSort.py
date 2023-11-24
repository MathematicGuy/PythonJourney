import random

"""
Imagine bubble rise on top then stack its to one side
1. Pick first value. Until the end:
    a. If the next value is larger or equal, pick that value.
    b. If the next value is smaller swap values.
"""
list_to_sort = []
# 4,3,7,6,2,5,1

bubble_length = int(input("Bubble list length: "))
for i in range(bubble_length):
    print('Num list: {}'.format(list_to_sort))
    given_num = int(input(f"Enter a num : "))

    # list_to_sort.append(random.randint(0, bubble_length))
    list_to_sort.append(given_num)


def BubbleSort(lts):
    # create a border seize for each next number
    # iterate the list
    for border in range(len(lts) - 1, 0, -1):  # len(lts) - 1 to make room for adjacent numbers
        for current_pos in range(border):
            adjacent_pos = current_pos + 1
            if lts[current_pos] >= lts[adjacent_pos]:
                lts[current_pos], lts[adjacent_pos] = lts[adjacent_pos], lts[current_pos]
    return lts

bs = BubbleSort(lts=list_to_sort)
print(bs)