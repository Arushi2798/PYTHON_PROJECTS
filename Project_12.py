"""question : The Birthday Paradox, also called the Birthday Problem, is the surprisingly high probability 
that two people will have the same birthday even in a small group of people. In a group of 70 people, 
there’s a 99.9 percent chance of two people having a matching birthday. But even in a group as small as
23 people, there’s a 50 percent chance of a matching birthday. This program performs several probability experiments
to determine the percentages for groups of different sizes. We call these types of experiments,
in which we conduct multiple random trials to understand the likely outcomes, Monte Carlo experiments."""


import datetime, random

print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com 
The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.
 
(It's not actually a paradox, it's just a surprising result.)''')

month=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
# date=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

num = int(input("\nhow many birthday's should i generate? (Max 100) \n >"))

if num <=100 and num >0:
    pass
else:
    print('enter a valid number')

print(f'\nHere are {num} birthdays')