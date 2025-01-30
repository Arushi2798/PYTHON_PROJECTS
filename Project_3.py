#Question Statement
"""Creating a Hangman Game: a guessing game which help identify the letters of a word.
the number of chances are only 6 as it needs the hangman figure to be complete."""

# import time
import random

words={1: "apple", 2: "blanket", 3: "bottle", 4: "towel", 5: "books", 6: "paper", 7: "kettle", 8: "tablet", 9: "mobile", 10: "vinegar",
       11:"Pillow",12:"greentea",13:"mirror",14:"school"}

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
            man = " O" 
            return man
        if wrong==2:
            man = " O\n/"
            return man
        if wrong==3:
            man = " O\n/|"
            return man
        if wrong==4:
            man = " O\n/|\\"
            return man
        if wrong==5:
            man = " O\n/|\\\n/"
            return man
        if wrong==6:
            man = " O\n/|\\\n/ \\"
            return man
        
        # time.sleep(1)

#to fill the blank for correct guess
def guesses(guess,count):
    wrong_count=count
    # print(guess)
    if guess in correct_word.lower():
        new=""
        i=correct_word.index(guess)
        for j in range(len(correct_word)):
            if j==i:
                new+=guess
            else:
                new+= s_word[0][j]
        # s_word[0] = guess
        return new
        
    else:
        wrong_count += 1
        print(f"Wrong guess\nyou have {6-wrong_count} guess left")
        hangman_img=(hangman(wrong_count))
        print(hangman_img)
        return wrong_count


print("Welcome to the HANGMAN Game Folks!!")
print("RULES: 1. Guess the word in 6 chances.\n \nYour WORD to guess is:")

s_word=word()
print(s_word[0])
print(s_word[1])

correct_word=s_word[1]
wrong_count=0

print("you have 6 guess")
guess = input("guess a letter: ")


while wrong_count!=6:
    ans=guesses(guess,wrong_count)
    if ans in [1,2,3,4,5,6]:
        wrong_count=ans
    else:
        guess=ans
    # print(ans)
    guess=input("next guess: ")

print("GAME OVER!!")

# print(f"the selected word is {s_w[1]}")
# wrong_count=int(input("wrong count :"))
# print(hangman(wrong_count))