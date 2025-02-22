print("Welcome to the STARBUCKS COFFEE!!")
choice=input("What would you like to have? (latte/espresso/cappuccino): ")
print("Please insert coins now")
coin_5=int(input("How many 5Rs. coins? : "))
coin_10=int(input("How many 10Rs. coins? : "))
coin_20=int(input("How many 20Rs. coins? : "))

l=150
c=175
e=200
sp=-1

money=coin_10*10 + coin_20*20+coin_5*5

match(choice):
    case "latte":
        if money>l:
            sp=money -l
        else:
            print(f"please give Rs{l-money} more")
    case "espresso":
        if money>e:
            sp=money -e
        else:
            print(f"please give Rs{e-money} more")
    case "cappuccino":
        if money>c:
            sp=money -c
        else:
            print(f"please give Rs{c-money} more")

if sp>=0 :
    print(f"Here's your change of {sp} rupees")