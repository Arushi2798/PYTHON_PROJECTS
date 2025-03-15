# # to install the dependent modules aas per the book requirements
# import subprocess
# import sys

# subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"], check=True)
# subprocess.run([sys.executable, "-m", "pip", "install", "bigbookpython"], check=True)
#check if insatlled correctly by importing pyperclip , bext


####
"""question: In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues. 
The game offers one of the following hints in response to your guess: “Pico” when your guess has a correct digit in the wrong place,
 “Fermi” when your guess has a correct digit in the correct place, and “Bagels” if your guess has no correct digits. 
 You have 10 tries to guess the secret number."""

import random

print("\nBagels, a deductive logic game.\nBy Al Sweigart al@inventwithpython.com \n\nI am thinking of a 3-digit number. Try to guess what it is.")
print("Here are some clues: \n When I say:    That means:\n  Pico         One digit is correct but in the wrong position.\n  Fermi        One digit is correct and in the right position.\n  Bagels       No digit is correct.")

max_digits=3
again= 'yes'


number =str(random.randint(100,999))
print(number)
correct=0
print("\nI have thought up a number.\nYou have 10 guesses to get it.")

def fermi(number,guess,correct):
    for j in range(max_digits):
        if number[j]==guess[j]:
            correct+=1
    return correct

def pico(number, guess,correct):
    for j in range(max_digits):
        for k in range(max_digits):
            if j!=k:
                if number[j]==guess[k]:
                    correct+=1
    return correct


    while again='yes':
    for i in range(10):
        guess= input(f'Guess #{i+1}: ')
        if len(guess) != max_digits:
            print("give a 3 digit number please")
        elif guess == number:
            print("You got it!")
            again=input("Do you want to play again? (yes or no): ")
            if again== 'no':
                print("Thanks for playing")
                break
        else:
            f=fermi(number,guess,correct)
            if f!=0:
                print('Fermi! '*f)
            else:
                p=pico(number,guess,correct)
                if p !=0:
                    print('Pico! '*p)
                else:
                    print("BAGELS !!!")