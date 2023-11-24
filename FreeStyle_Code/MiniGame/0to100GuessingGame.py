import random



def hint(player_guess, rn):
    if 0 < (player_guess - rn) < 3:
        print("So close")
    elif 0 < (player_guess - rn) <= 10:  # 50 42 = 8
        print("A little lower")
    elif -10 <= (player_guess - rn) < 0:  # 50 60 = -10
        print("A little higher")
    elif (player_guess - rn) > 10:  # 50 38 = 12
        print("Too high")
    elif (player_guess - rn) < -10:  # 50 69 = -19
        print("Too low")


play = True
while play:
    health = 0
    difficulty = input("choose a level. Type 'easy' or 'hard':").lower()
    if difficulty == 'easy':
        health = 10
    elif difficulty == 'hard':
        health = 5

    rn = random.randint(0, 100)
    random_num = rn
    print("The number is between 1 and 100")
    print("-------------------------------------------------------------")

    not_winning = True
    while not_winning:
        print("the rn are: ", random_num)

        guess = int(input("Guess the number: "))

        if guess != random_num:
            health -= 1
            print(f"You have {health} life left")
        elif guess == random_num:
            print("Correct, You Won")
            not_winning = False

        if health == 0:
            print("You lose")
            not_winning = False

        hint(guess, random_num)
        print("================================================================")
    again = str(input("do you want to play again. Type 'yes' or 'no': "))
    if again == "no":
        play = False
