#Question Statement
"""Creating a Hangman Game: a guessing game which help identify the letters of a word.
the number of chances are only 6 as it needs the hangman figure to be complete."""

# import time
import random

words={1: "apple", 2: "blanket", 3: "bottle", 4: "towel", 5: "books", 6: "paper", 7: "kettle", 8: "tablet", 9: "mobile", 10: "vinegar",
       11:"pillow",12:"greentea",13:"mirror",14:"school", 15: "laptop"}

#creating blanks spaces for total letter count of any word
def word():
    selected_word=words.get(random.randint(1,len(words)))
    # print(selected_word)
    blank="_"*len(selected_word)
    return blank,selected_word

#to draw the hangman figure
def hangman(wrong):
    man=""
    while wrong<7: 
        if wrong==1:
            man = " |----\n O   |\n     |\n     |\n     |\n     |\n-------" 
            return man
        if wrong==2:
            man = " |----\n O   |\n/    |\n     |\n     |\n     |\n-------"
            return man
        if wrong==3:
            man = " |----\n O   |\n/|   |\n     |\n     |\n     |\n-------"
            return man
        if wrong==4:
            man = " |----\n O   |\n/|\\  |\n     |\n     |\n     |\n-------"
            return man
        if wrong==5:
            man = " |----\n O   |\n/|\\  |\n/    |\n     |\n     |\n-------"
            return man
        if wrong==6:
            man = " |----\n O   |\n/|\\  |\n/ \\  |\n     |\n     |\n-------"
            return man
        
        # time.sleep(1)

#to fill the blank for correct guess
def guesses(blank,guess,wrong_count):
    if guess in correct_word.lower():

        l=[]
        for i in range(len(correct_word)):
            if guess== correct_word[i]:
                l.append(i)
        for j in l:
            blank[j]=guess
        return blank
        
    else:
        wrong_count += 1
        print(f"Wrong guess\nyou have {6-wrong_count} guess left")
        hangman_img=(hangman(wrong_count))
        print(hangman_img)
        return wrong_count


print("         Welcome to the HANGMAN Game Folks!!")
print("     RULES: 1. Guess the word in 6 chances.\n \nYour WORD to guess is: ")

s_word=word()
print(s_word[0])

correct_word=s_word[1]
wrong_count=0

print("\n you have 6 guess")
guess = input("\n guess a letter: ")

blank=list(s_word[0])

while wrong_count < 6:
    ans=guesses(blank,guess,wrong_count)
    if ans in [1,2,3,4,5,6]:
        wrong_count=ans
    else:
        word=ans
        print(ans)
        if "_" not in word:
            wrong_count=6
            print(f"        YOU WON!! \n    Congratulations!!!! ")
    if wrong_count==6 :
        break
    else:
        g=input("\n next guess: ")
        guess=g.lower()

print("         GAME OVER!!")
print(f'the correct word was {s_word[1]}')