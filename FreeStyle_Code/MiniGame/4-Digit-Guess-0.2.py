"""
4 Digit Number Guessing Game

- RULE -
+ Given 4 digits number
+ Player must guess 4 digits in a row. ( Until all digit are correct )
+ If any digit are correct -> return total correct digit & correct digit at right position

 Ex:
 random_num = [4345]
 guess = 4555
 >> The Correct number is 4. In position 1
"""

import random

''' cho 1 số random có 4 chữ số'''
random_digit = []  # 4 different digit


def generate_random():
    print('=========================================')
    random_digit.clear()
    while len(random_digit) < 4:
        num = random.randint(1, 9)
        if num not in random_digit:
            random_digit.append(num)


generate_random()

total_correct_guess = 0
total_correct_position = 0


def guess_and_score(correct_guess, correct_position):
    print(f"pshaws, the random number are {random_digit}")  # gợi ý
    print('=========================================')

    try:
        guess = input('Enter 4 random digit: ')  # input take value as str
        player_guess = []  # '8j22'

        ''' Tách giá trị (của guess) '''
        for x in guess:  # for loop read every item in guess. '9323' -> '9', '3', '2', '3'
            if x == " ":  # if there space " " in guess -> don't care, continue
                continue
            else:
                player_guess.append(x)  #

        ''' Check more than 4 input error '''
        if len(player_guess) > 4:
            print("pls enter 4 digit")

        ''' Check duplicate digit '''
        set_player_guess = set(player_guess)
        if len(set_player_guess) != len(player_guess):
            print("No duplicate digit, pls enter again")
            guess_and_score(0, 0)

        print(f"guess: {player_guess}")

        ''' Attention: (digit is int) & (guess is str)'''
        ''' Catch str input '''
        for digit in random_digit:  # Compare each digit to every guess value
            for guess in player_guess:
                ''' Calculate Score '''
                # return that number and value
                if str(digit) == guess:
                    correct_guess += 1
                    '''bug -> guess là str. items trong player_guess là int'''
                    if random_digit.index(int(guess)) == player_guess.index(guess):
                        correct_position += 1

                    if correct_guess == 4:
                        print(f'All guess are right, the right answer is {player_guess}')
                        restart = input('Enter to restart, "n" to quit: ')
                        if restart == "n":
                            pass
                        else:
                            generate_random()
                            guess_and_score(0, 0)

        print(f"Correct Guess: {correct_guess} ")
        print(f"Correct position: {correct_position}")

        if correct_guess != 4:
            guess_and_score(0, 0)

    except ValueError as player_guess:
        print(f"{player_guess} isn't a number you dumb dumb")


guess_and_score(0, 0)
