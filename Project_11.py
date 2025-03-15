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

number =random.randint(100,999)
# print(number)

print("\nI have thought up a number.\nYou have 10 guesses to get it.")



for i in range(10):
     guess= int(input(f'Guess #{i+1}: '))
    