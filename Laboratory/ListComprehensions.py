def EvenNumber(num):
    ''' List comprehension '''
    a = [
        x ** 2  # Expression
        for x  # Variable name
        in range(num)  # in iterable
        if x % 2 == 0  # if condition
    ]
    return a


print(EvenNumber(22))
