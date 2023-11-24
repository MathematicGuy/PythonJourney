logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''



Bidding_log = {} 



def Compare(Bidding_log):
    highest_bid = 0
    winner = ""
    #Bidding_log = {'josh':220, 'Kevin':490}
    for i in Bidding_log:
        if Bidding_log[i] > highest_bid:
            highest_bid = Bidding_log[i]
            winner = i
    print(f'{winner} is the on with the highest bid {highest_bid}')
        
finishBid = False
while not finishBid: 
    print(logo)
    name = input('Bidder name: ')
    money = int(input('What are your bid: $'))
    Bidding_log[name] = money
    anotherBidder = input('Is there another Bidder, type "Y" or "N": ').lower()
    
    if anotherBidder == "n":
        Compare(Bidding_log)
        finishBid = True
    