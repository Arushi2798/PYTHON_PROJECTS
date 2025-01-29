#Question Statement
"""Creating a password generator"""

import random

print("WELCOME TO PASSWORD GENERATOR!")
letter=int(input("How many letters would you like in your password? \n "))
symbol=int(input("How many symbols would you like in your password? \n "))
number=int(input("How many numbers would you like in your password? \n "))

passw = ""
password=[]

for item in range(letter):
    password.append(random.choice("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"))
for item in range(symbol):
    password.append(random.choice('!@#$%^&*()~`-_{}|:<>?[]\;,./'))
for item in range(number):
    password.append(random.randint(0,9))
# print(password)
random.shuffle(password)
for i in password:
    passw += str(i)

print(passw)