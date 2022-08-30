import os
from logo import logo,logo1,logo2

print(logo)
print(logo1)

bids={}
bidding_finish=False

def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        amt=bidding_record[bidder]
        if amt>highest_bid:
            highest_bid=amt
            winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}\n")

while not bidding_finish:
    name=input("What is your name? \n")
    price=int(input("What is your bid? $"))
    bids[name]=price
    user_input=input("Is there any other user? Yes/No \n").lower()
    if user_input=='no':
        bidding_finish=True
        print(logo2)
        find_highest_bidder(bids)
    elif user_input=='yes':
        os.system('CLS')

