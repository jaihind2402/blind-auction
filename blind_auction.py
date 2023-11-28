import os


from art import logo_build_auction

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen

def find_highest_bidder(dict_of_list: dict):
    highest_bid = 0
    winner = ''
    for k in bid_dict:
        money = bid_dict[k]
        # highest_bid = value
        # highest_bid+=highest_bid
        if money> highest_bid:
            highest_bid = money 
            winner = k
        
    print(f"The winner is {winner}  with a bid of ${highest_bid}")

print(logo_build_auction)
print("Welcome to the bind auction ")
bid_dict = {}
flag = 1
while flag:
    name = input("What's your name?: ")
    value = int(input('What is your bid?: '))
    bid_dict.update({name:value})
    # print(f"bid dict {bid_dict}")
    next_entry = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if next_entry == 'no':
        flag = 0
        find_highest_bidder(bid_dict)
        break
    else:
        cls()
        bid_dict.update({name:value})
    # print(bid_dict)
# print()
# print(f"bid dict out of loop {bid_dict}")

    # else:
    #     print(f"The winner is {k} with a bid of {money}")

