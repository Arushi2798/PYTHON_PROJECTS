print("Welcome to the STARBUCKS COFFEE!!")
choice=input("What would you like to have? (latte/espresso/cappuccino): ")
print("Pleas einsert coins now")
coin_5=int(input("How many 5Rs. coins? : "))
coin_10=int(input("How many 10Rs. coins? : "))
coin_20=int(input("How many 20Rs. coins? : "))

l=150
c=175
e=200

money=coin_10*10 + coin_20*20+coin_5*5
match(choice):
    case "latte":
        sp=l-money
    case "espresso":
        sp=e-money
    case "cappuccino":
        sp=c-money