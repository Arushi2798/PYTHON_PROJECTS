#Question Statement
"""Creating A silent Auction Program: bidding is performed silently, where each other's bid is not known.
the highest bid wins."""


import os
print(" ******WELCOME TO THE GAME OF SILENT AUCTION PROGRAM******")

def result(NAME,BID):
    win=max(BID)
    win_id=BID.index(win)
    winner=NAME[win_id]
    return winner,win


more="yes"
NAME=[]
BID=[]
while more=="yes":
    name=input("what's your name?:  ")
    bid=int(input("what's your bid?:  "))
    NAME.append(name)
    BID.append(bid)
    more=input("Is there any other bidders? TYPE 'yes' or 'no' \n").lower()
    if more=="yes":
        os.system("cls")
    else:
        winner=result(NAME,BID)
        os.system("cls")

print(f"the winner is {winner[0]} with the bid of {winner[1]} amount")