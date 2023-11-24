logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

# +-x/ continue using the ans

total = [0]     #Use list to import value in function (def sign())
#function for each math key
def addition(a,b,total): 
    sum = float(a+b)
    total[0] = (sum)             #total save sum value
    return (f"a + b = {sum}")

def subtraction(a,b,total):
    sum = float(a - b)
    total[0] = (sum)
    return (f"a - b = {sum}")

def multiply(a,b,total):
    sum = a*b
    total[0] = (sum)
    return (f"a*b = {sum}")

def divide(a,b,total):
    sum = a / b
    total[0] = (sum)
    return (f"a*b = {sum}")

#Calc calculate is True. Calc with previous sum when Carried is True 
calculate = True
Carried = False

def mathSign():
    sign = ["+","-","*","/"]
    for i in (sign):
        print(i)

#catching math-operation-input function 
def choosing_operation(a,operation,b):
    match operation:
        case '+':
            print(addition(a,b,total))
            
        case '-':
            print(subtraction(a,b,total))
            
        case '*':
            print(multiply(a,b,total))
            
        case '/':
            print(divide(a,b,total))

#Create 2 scenario: Calc & Calc with the previous sum 
while calculate:
    #Calc with no Carry
    if Carried == False: 
        a = int(input("Enter 1st number: "))
        mathSign()
        operation = input("Enter the first operation: ")
        b = int(input("Enter 2nd number: "))

        #Calling function with given operation-input
        choosing_operation(a,operation,b)

    #Calc with Carry as long as Carried is True. Repeat infinity unless carry == "n"  
    elif Carried == True:
        
        while Carried:
            a = total[0]       #Set a as the previous calc Sum
            mathSign()
            operation = input("Enter the operation: ")
            b = int(input("Enter 2nd number: "))

            choosing_operation(a,operation,b)
            
            #Ask the user if they want do continue. Return Carry is False if input is "n"
            carry = input(f"Do you want to continue with {total[0]}. type 'Y' or 'N': ").lower()      
            if carry == "y":
                continue 
            elif carry == "n": 
                Carried = False
            print(total)
    
    #Continue is run if there no interruption (Such as a Carried == True while loop. )
    #Ask the user to calc like Normal or Quit. Print final ans
    carry = input(f"Do you want to continue with {total[0]}. type 'Y' or 'N': ").lower()
    if  carry == "y":
        Carried = True
    elif carry == "n": 
        total = 0
        calculate = False
        print(f"final result = {total}")    