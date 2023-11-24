# from logo import logo
#TODO-1: Fix the money system
'''
make Your_Hand appear when Deal
Check the Bust/Black Jack

'''

import random
play = True
game_continue = True
have_not_deal = True

bot_hand = []
player_hand = []

bot_score = [0]
player_score = [0]

Banks = [1200]
Current_bet = [0]


''' Fundamental BJ function '''
#Adding 2 card to both player hand
def card_in_hand():
    print(f"Your hand: {player_hand}")
    print(f"Bot hand: {bot_hand}")

#TODO-2: Create a Betting system provide (player & Bot) Bet_amount.
# note: Create auto bet_range -> Type {bet_range} 5->10k

def break_line():
    print("-------------------------------------------------")

#TODO- Optimizing Score Comparing algorithm
'''Score Function - Calc Score,etc..'''  
def Ace(chosen_score,chosen_hand):
    for card in chosen_hand:   
        if card == "A":
            if ((player_score[0] or bot_score[0]) + 10) <= 21:
                chosen_score.append(10) 
            elif (chosen_score + 10) > 21:
                chosen_score.remove(11)
                chosen_score.append(1)
            elif isinstance(i,str):      #converse J,Q,K,A value to 10
                chosen_score.append(10)
            elif isinstance(i,int):
                chosen_score.append(i)

def burstAndBlackjack():
    
    if player_score[0] == 21  and player_score[0] == bot_score[0]:
        return print("Black Jack, You Lose")
    elif bot_score[0] == 21 and player_score[0] == bot_score[0]:
        return print("Black Jack, You Won")

    '''Burst'''
    if player_score[0] > 21:
        print("You Burst")
        return game_continue is False
    elif bot_score[0] > 21:
        print("Bot Burst")
        return game_continue is False

def compare(): 
    Ace(player_score[0],player_hand)
    Ace(bot_score,bot_hand)
  
    print(f"Player score: {player_score}")
    print(f"Bot score: {bot_score}")
    break_line()

    burstAndBlackjack()

    if player_score[0] > bot_score[0]:
        print("You Won")
    elif player_score[0] == bot_score[0]:
        print("Draw")
    else: 
        print("You lose")

    break_line()
    keep_playing = input("Keep playing. Type 'Y' or 'N': ").lower()
    if keep_playing == "n":
        return 
    
'''Game function'''
def deal_card():
    Deck = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
    random_card = random.choice(Deck)    

    return random_card


for i in range(2):
    player_hand.append(deal_card())
    bot_hand.append(deal_card())

def game_start(player_score,bot_score):
    burstAndBlackjack()  
    
    player_choice = str(input("Hit or Stand: ")).lower() 
    print(bot_score[0])
        
    if player_choice == "hit":
        player_hand.append(deal_card())
        
        if bot_score[0] < 17:
            print(f"bot_score: {bot_score[0]}")
            bot_hand.append(deal_card())
        elif bot_score[0] >= 17:
            print("Bot choose to Stand")    

    elif player_choice == "stand":
        compare()
    
    bot_score[0] = sum(bot_hand)
    player_score[0] = sum(player_hand)

    card_in_hand()
    

def betting(Banks,Current_bet,player_score,bot_score):
    print("How much do you want to bet. Type 5 10 25 50 100 250")
    bet_amount = int(input("> $"))

    ''' Adding money ''' #Problem: bet_amount take value as str in default. Find a way to feed back if bet_amount not an int 
    Current_bet[0] += bet_amount
    Banks[0] -= bet_amount

    print(f"Current Bet: {Current_bet[0]}")
    print(f"Banks: {Banks[0]}")
    break_line()

    confirm = input('Type "Deal" if  finished. "Enter" to continue: ').lower()
    break_line()

    ''' Deal or Continue '''
    if confirm == "deal":    
        while game_continue:
            game_start(player_score,bot_score)    

    
# print(logo)
while play:
    card_in_hand()
    break_line()
    
    betting(Banks, Current_bet,player_score[0],bot_score[0])
    
    