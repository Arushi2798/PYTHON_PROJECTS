print("Welcome to the STARBUCKS COFFEE!!")
choice=input("What would you like to have? (latte/espresso/cappuccino): ")


def orderplaced():
    print("Please insert coins now")
    coin=[5,10,20]
    m=0
    for each in coin:
        coin=int(input(f"How many {each}Rs. coins? : "))
        m+=coin*each
    return m


def pricecal(money):
    price={"latte":150,"espresso":200,"cappuccino":175}

    match(choice):
        case "latte":
            sp=money-price.get("latte")
        case "espresso":
            sp=money-price.get("espresso")
        case "cappuccino":
            sp=money-price.get("cappuccino")

    return sp


def changecal(sp,money):
    if sp<0:
        print(f"please give Rs{-sp} more")
        extra=orderplaced()
        money += extra
        new=pricecal(money)
        changecal(new, money)
    elif sp>0 :
        print(f"Here's your change of {sp} rupees")
        print("Enjoy your drink")
    else:
        print("Enjoy your drink")


money = orderplaced()
sp= pricecal(money)
change= changecal(sp,money)