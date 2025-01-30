#Question Statement
"""Creating a Rock Paper Scissor GAME. 
RULES: 1. rock wins against scissor,
       2. scissor wins against paper,
       3. paper wins aginst rock. 
       """
#notation: 0 for rock, 1 for paper, 2 for scissor

import random

print("Welcome to the ROCK-PAPER-SCISSOR Game Folks!!")
print("RULES: \n1. rock wins against scissor,\n2. scissor wins against paper,\n3. paper wins aginst rock.")

res="y"
while res.lower() == "y" :
    user= int(input("what will you choose? \n 0-> rock\t 1-> paper \t 2->scissor \n"))
    if user>2:
        res=input("INVALID INPUT!!!!.\n wanna try  again with correct input values? ")
    com= random.randint(0,2)
    if user == com:
        res=input("it's a TIE.\n wanna try  again? ")
    elif com==0:
        if user==1:
            res=input("YOU WIN.\n wanna try  again? ")
        elif user ==2:
            res=input("YOU LOOSE.\n wanna try  again? ")
    elif com==1:
        if user==0:
            res=input("YOU LOOSE.\n wanna try  again? ")
        elif user ==2:
            res=input("YOU WIN.\n wanna try  again? ")
    elif com==2:
        if user==0:
            res=input("YOU WIN.\n wanna try  again? ")
        elif user ==1:
            res=input("YOU LOOSE.\n wanna try  again? ")

