"""question : The Birthday Paradox, also called the Birthday Problem, is the surprisingly high probability 
that two people will have the same birthday even in a small group of people. In a group of 70 people, 
there’s a 99.9 percent chance of two people having a matching birthday. But even in a group as small as
23 people, there’s a 50 percent chance of a matching birthday. This program performs several probability experiments
to determine the percentages for groups of different sizes. We call these types of experiments,
in which we conduct multiple random trials to understand the likely outcomes, Monte Carlo experiments."""


import datetime as d
import random

def getbirthdays(number):
    dates=[]
    for i in range(number):
        startyear=d.date(2024,1,1)
        randomday = d.timedelta(days=random.randint(0,365))#to generate a new date after randomly selecting a time difference between 0 to 365 days
        caldates = startyear+randomday
        newmonth = MONTHS[caldates.month-1]
        newday=caldates.day
        newdate= newmonth +" "+ str(newday)
        dates.append(newdate)

    return dates

def getMatch(birthdates):
    c=[]
    for i in range(len(birthdates)):
        for j in range(i+1,len(birthdates)):
            if birthdates[i] ==birthdates[j]:
                c.append(i)
    return c


print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com 
The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.
 
(It's not actually a paradox, it's just a surprising result.)''')

MONTHS=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# date=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

num = int(input("\nhow many birthday's should i generate? (Max 100) \n >"))

if num <=100 and num >0:
    pass
else:
    print('enter a valid number')

print(f'\nHere are {num} birthdays')
birthdates = getbirthdays(num)
# for each in birthdates:
#     print(each, end=", ")

print(", ".join(birthdates), end='')

"""for similar effects use following when the fucntion only returns list of dates without modifications
for i, birthday in enumerate(birthdays):
      if i != 0:
          # Display a comma for each birthday after the first birthday.
          print(', ', end='')
      monthName = MONTHS[birthday.month - 1]
      dateText = '{} {}'.format(monthName, birthday.day)
      print(dateText, end='')
  print()
  print()"""

#to check for matching birthdays
match=getMatch(birthdates)
if len(match)==0:
    print("\nIn this simulation, there are no matching birthdays.")
else:
    date=[]
    for each in match:
        date.append(birthdates[each])
    
    print(f"\n\n In this simulation, multiple people have a birthday on {", ".join(date)}. \n")

#to run 100,000 simulations
# Run through 100,000 simulations:
print(f'Generating {num} random birthdays 100,000 times...')
input('Press Enter to begin...')
print('Let\'s run another 100,000 simulations.')