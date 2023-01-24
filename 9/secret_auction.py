import os 
from art import logo
from time import sleep

auction_running = True
bidders = {}

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

clear()

print(logo)
print('Welcome to secret auction!')
sleep(2)

def find_highest_bidder(bidding_record: dict):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    return [winner, highest_bid]

while auction_running is True:
    clear()
    name = input("What is your name? ")
    bid = int(input("What would you like to bid? $"))

    bidders[name] = bid

    continue_bid = input("Any more bidders out there? Yes or No... ")

    if(continue_bid.lower() == 'no'):
        highest_bidder = find_highest_bidder(bidders)
        print(f"The winner is {highest_bidder[0]} with a total amount of ${highest_bidder[1]}\nCongratulations!")
        print('Participants:')
        for bidder in bidders:
            print(f"{bidder}, ${bidders[bidder]}")
        auction_running = False
