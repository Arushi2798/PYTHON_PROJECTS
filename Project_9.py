print("Welcome to the STARBUCKS COFFEE!!")
choice=input("What would you like to have? (latte/espresso/cappuccino): ")
print("Pleas einsert coins now")
coin_5=int(input("How many 5Rs. coins? : "))
coin_10=int(input("How many 10Rs. coins? : "))
coin_20=int(input("How many 20Rs. coins? : "))

l=150
c=175
e=200

def switch(choice):
    case choice=="latte":
        