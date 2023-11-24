#OverThinking be like   
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
# Context & Input
def origin():
    print(logo)
    print('Welcome to the annual Black Market Auction ')
    bidder = str(input("What is your name: "))
    bid = int(input('What are your Bid: $ '))

    auction_dict['name_list'].append(bidder)            #Appending values to ['tyler','sherlock','watson'] nested list  in 'name_list' dictionary
    auction_dict['bid_list'].append(bid)                #Appending values to ......  


#TODO-1: In in auction_list make a nested list for name and bid. Get key and value from it
auction_dict = {'name_list':['sherlock','watson'], 'bid_list':[291,2221]} 
#Adding name & bid values to auction_dict


#TODO: Problem -> adding input to auction_dict
      

#Get key and value
list_key = list(auction_dict.keys())            #get key
first_bid = auction_dict['bid_list'][0]         #get 1st bid value
first_bidder = auction_dict['name_list'][0]     #get 1st bidder name value



#TODO-2: Compare each bid  & print out the Highest bid
Highest = []    #get the first values in list, Compare it to another num. If Higher replace its place
Winner = []     
Highest.append(first_bid)
Winner.append(first_bidder)

#Define Highest[0] as HighestBid for transparent understanding
HighestBid = Highest[0]
WinnerBidder = Winner[0]

def Compare(Winner, Highest):
    #List all values of key in auction_dict
    for i in auction_dict['bid_list']:  # i == name_list  Ex: i == 'sherlock
        if i > Highest[0]:              # Compare current bid to highest bid in Highest (Current <-> first bid in bid_list)
            Highest[0] = i

            #get the same ['name_list'][i] as ['bid_list'][i]
            win_pos = auction_dict['bid_list'].index(i)
            Winner[0] = auction_dict['name_list'][win_pos]

            
#TODO-3: Adding another Bidder (with while loop)


while True:
    origin()
    Compare(Winner,Highest)
    more = str(input('is there anymore bidder "Y" or "N":').lower())

    print(f"name list: {auction_dict['name_list']}")
    print(f"bid list: {auction_dict['bid_list']}")


    match more:
        case 'n':
            print(f'{WinnerBidder.upper()} is the one who pay the highest {HighestBid}')
            break
        case _:
            continue


    # print(f'{Winner} is the one who pay the highest {Highest}')
    
    


