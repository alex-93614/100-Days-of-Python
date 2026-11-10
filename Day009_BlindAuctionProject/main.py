#Blind Auction Project

import os
import art

def clear_screen():
    print("\n" * 100)
    # pycharmではうまくいかない↓
    # if os.name == 'nt':
    #     os.system('cls')
    # else:
    #     # os.system('clear')
    #     print('\033[2J\033[H', end='')

print(art.logo)
bidder={}
loop = True
while loop:
# TODO-1: Ask the user for input
    name = input("What is your name?: ")
    bit = int(input("What is your bit?: $"))
# TODO-2: Save data into dictionary {name: price}
    bidder[name] = bit
# TODO-3: Whether if new bids need to be added
    loop = input("Are you any other bidders? Type 'yes' or 'no'. ")
    if loop.lower() == "yes":
        loop = True
    else:
        loop = False
    clear_screen()
# TODO-4: Compare bids in dictionary
highest_bid = 0
winner = ""
for bid in bidder:
    if bidder[bid] > highest_bid:
        highest_bid = bidder[bid]
for bid in bidder:
    if bidder[bid] == highest_bid:
        winner = bid
print(f"The winner is {winner} with a bid of {highest_bid}")

