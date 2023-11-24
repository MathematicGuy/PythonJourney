#Prime Number

#Prime only divided by 1 and itself
# To check -> divided to every number smaller than its


# A way to compare (a and a + 2) in for loop
def IsPrime(a,b):
    for larger in range(a,b):
        if larger > 1:                          
            for smaller in range(2,larger):     # Error if smaller range from 1. Because num % 1 alway == 1.
                if larger % smaller == 0:       # calculate the remainder 
                    break                       #skip into the next code 
            else:
                print(larger)

IsPrime(0,101)
     
    






