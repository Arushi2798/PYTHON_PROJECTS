print("Welcome to the STARBUCKS COFFEE!!")
choice=input("What would you like to have? (latte/espresso/cappuccino): ")
print("Please insert coins now")

def orderplaced():
    coin=[5,10,20]
    m=0
    for each in coin:
        coin=int(input(f"How many {each}Rs. coins? : "))
        m+=coin*each
    return m

money=orderplaced()

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

sp=pricecal()

def changecal(sp):
    if sp<0:
        print(f"please give Rs{-sp} more")
        extra=orderplaced()
        total=sp + pricecal(extra)
        changecal(total)
    elif sp>0 :
        print(f"Here's your change of {sp} rupees")
        print("Enjoy your drink")
    else:
        print("Enjoy your drink")