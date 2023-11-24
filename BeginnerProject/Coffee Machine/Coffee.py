from coffeeResource import *

def totalMoney():
    print('Pls insert coins:')
    quarters = int(input('How many quarter: '))
    dimes = int(input('How many dimes: '))
    nickles = int(input('How many nickle: '))
    pennies = int(input('How many pennies: '))

    return 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies


def is_resources_sufficient(order_drink):
    orderIngredient = MENU[order_drink]['ingredients']

    for items in orderIngredient:  # compare order ingredient with stock ingredient
        if resources[items] < orderIngredient[items]:
            print(f"Sorry, {items} is out of Stock")
        else:
            resources[items] -= orderIngredient[items]


def budget(payment, order_drink):
    coffeeCost = MENU[order_drink]['cost']
    global profit
    ''' Calculate if payment == coffee cost '''
    if payment < coffeeCost:
        print(f"Sorry that not enough for {order_drink.upper()}")
        print(f"Here your changes {round(payment, 3)}")
    elif payment >= coffeeCost:
        payment -= coffeeCost
        profit += payment
        print(f"Here your {order_drink.upper()} and change {round(payment, 3)}, thank for coming")


profit = 0
On = True
while On:
    coffeeChoice = input("What would you like? (espresso/latte/cappuccino/milk coffee): ").lower()

    if coffeeChoice == "report":
        for info in resources:
            print(f'{info.capitalize()}: {resources[info]}')
        print(f'Total Money: {round(profit, 3)}')
    elif coffeeChoice == "off":
        On = False
    elif coffeeChoice == "import":
        marketChoice = input('Choose a product: ')
        productCost = market[marketChoice][0]
        productQuantity = market[marketChoice][1]

        if profit >= productCost:
            #Print market table
            profit -= productCost
            resources[marketChoice] += market[1]
            print(f"Import {productQuantity} {marketChoice} complete")
        elif profit < productCost:
            print('Not enough money')
    elif coffeeChoice not in MENU:
        print('Sorry that not in our Menu')
    else:
        total = totalMoney()
        budget(total, coffeeChoice)
        is_resources_sufficient(coffeeChoice)





