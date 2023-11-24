import random

# create a deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(s, r) for s in suits for r in ranks]

# initialize the player's hand and dealer's hand
player_hand = []
dealer_hand = []

# define function to calculate the value of a hand
def calculate_hand(hand):
    total = 0
    num_aces = 0
    for card in hand:
        rank = card[1]
        if rank.isdigit():
            total += int(rank)
        elif rank in ['Jack', 'Queen', 'King']:
            total += 10
        else: # Ace
            num_aces += 1
            total += 11
    while num_aces > 0 and total > 21:
        total -= 10
        num_aces -= 1
    return total

# deal two cards to the player and dealer
random.shuffle(deck)
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())

# show the player's hand and dealer's upcard
print("Player's hand:", player_hand)
print("Dealer's upcard:", dealer_hand[0])

# player's turn
while True:
    choice = input("Hit or stand? ")
    if choice.lower() == 'hit':
        player_hand.append(deck.pop())
        print("Player's hand:", player_hand)
        if calculate_hand(player_hand) > 21:
            print("Bust! Dealer wins.")
            quit()
    elif choice.lower() == 'stand':
        break

# dealer's turn
print("Dealer's hand:", dealer_hand)
while calculate_hand(dealer_hand) < 17:
    dealer_hand.append(deck.pop())
    print("Dealer hits:", dealer_hand)
    if calculate_hand(dealer_hand) > 21:
        print("Dealer busts! Player wins.")
        quit()

# compare hands
player_total = calculate_hand(player_hand)
dealer_total = calculate_hand(dealer_hand)
if player_total > dealer_total:
    print("Player wins!")
elif dealer_total > player_total:
    print("Dealer wins!")
else:
    print("Tie!")