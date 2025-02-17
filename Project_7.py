import random
print("Welcome to the GUESSING A NUMBER Game Folks!!")

guess=random.randint(0,50)
print("let me think of a number between 0 to 50.")
level=input("choose level of difficulty.... type 'easy' or 'hard'  ")
print(guess)
no_turn=0

if level=='easy':
    print("you have 10 attempts to guess the number!!")
    chance=10
elif level =='hard':
    print("you have 4 attempts to guess the number!!")
    chance=4

while no_turn < chance:
    c=chance
    no=int(input('make a guess: '))
    if no >guess:
        print("you guessed high")
        c-=1
        print("guess again")
    elif no< guess:
        print('you guessed low')
        c-=1
        print("guess again")
    elif no==guess:
        print("you are correct!!!")
        break     

    print(f"you have {c} chances left")
    no_turn+=1

print("GAME OVER!!!")