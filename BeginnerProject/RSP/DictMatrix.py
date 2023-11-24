import random

WinningStreak = 0

# 3 í unexpected inputs
# Player is ROW
# Bot is Column

# 0 is DRAW
# 1 is Lose
# 2 is Winning
rps_matrix = [
    [0, 2, 1],
    [1, 0, 2],
    [2, 1, 0],
    [3, 3, 3],
]

def rank():
    rank = ['Bronze','Silver','Gold','Platinum','Diamond','Amethyst','Master']

    if WinningStreak < 2:
        return rank[0]
    elif WinningStreak >= 4:
        return rank[1]
    elif WinningStreak >= 6:
        return rank[2]
    elif WinningStreak >= 8:
        return rank[3]
    elif WinningStreak >= 10:
        return rank[4]
    elif WinningStreak >= 12:
        return rank[5]

def result_and_score():
    global WinningStreak
    result_index = rps_matrix[player_index_choice][bot_index_choice]  # return 0 / 1 / 2 / 3
    if result_index == 2:  # Winning
        WinningStreak += 1
    elif result_index == 1:  # Losing
        WinningStreak = 0
    elif WinningStreak == 3:
        print('You Won, game end')

    print('Winning Streak: ', WinningStreak)
    result = ['Tie OvOb', 'You Lose :((', 'You Won :))', 'Invalid Input, pls choose another one']
    print(result[result_index])
    print()

play = True
while play:
    player_choice = input('Choose rock, paper or scissor: ').lower()
    if player_choice == 'rank':
        print('Your Current rank is: {}'.format(rank()))
    elif player_choice == 'stop':
        print('See You Later')
        play = False

    else:
        choice = ['rock', 'paper', 'scissor']
        bot_choice = random.choice(choice)

        choice_list = {
            'rock': 0,
            'paper': 1,
            'scissor': 2,
        }

        bot_index_choice = choice_list[bot_choice]
        player_index_choice = choice_list.get(player_choice, 3)  # return player_choice index else return 3

        result_and_score()
        print('The bot choose ', bot_choice)

