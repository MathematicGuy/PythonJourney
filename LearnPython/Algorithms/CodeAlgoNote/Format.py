def to_celsius(x):
    return (x-32)*5/9

for x in range(0, 101, 10):
    # to format, use :
    # >n to backspace n times
    # nf to print number after the dot (floating point with that many decimals)
    print('{:>3} F | {:>9.2f} C'.format(x, to_celsius(x)))


def to_integer(x):
    print('{:d}'.format(x))
to_integer('3232')