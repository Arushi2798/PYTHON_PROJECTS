print("Welcome to the STARBUCKS COFFEE!!")
choice=input("What would you like to have? (latte/espresso/cappuccino): ")
print("Please insert coins now")

coin=[5,10,20]
money=0
for each in coin:
    coin=int(input(f"How many {each}Rs. coins? : "))
    money+=coin*each

price={"latte":150,"espresso":200,"cappuccino":175}
sp=-1

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
    