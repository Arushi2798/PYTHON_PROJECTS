def orderplaced():
    print("Please insert coins now")
    coin=[5,10,20]
    m=0
    for each in coin:
        coin=int(input(f"How many {each}Rs. coins? : "))
        m+=coin*each
    return m


def pricecal(money):
    price={"latte":150,"espresso":100,"cappuccino":200}

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

print("Welcome to the STARBUCKS COFFEE!!")

resources={"Water":500,"Milk":500, "Coffee":50, "Money":0}

choice=1
while choice:
    res=0
    choice=input("What would you like to have? (latte/espresso/cappuccino): ")

    match choice:
        case "off":
            exit()
        case "report":
            for each in resources:
                print(f"{each} : {resources.get(each)}")

        case "latte":
            resources["Coffee"]=resources.get("Coffee")-24
            resources["Milk"]=resources.get("Milk")-150
            resources["Water"]=resources.get("Water")-200
            resources["Money"]=resources.get("Money")+150
            for each in resources:
                if resources.get(each) < 0:
                    res+=1
            if res!=0:
                print(f"Sorry, we don't have enough {each} right now,\n you can order something else")
                choice=input("What would you like to have? (latte/espresso/cappuccino): ")
                money = orderplaced()
                sp= pricecal(money)
                change= changecal(sp,money)

            else:
                money = orderplaced()
                sp= pricecal(money)
                change= changecal(sp,money)
            
        case "cappuccino":
            resources["Coffee"]=resources.get("Coffee")-24
            resources["Milk"]=resources.get("Milk")-100
            resources["Water"]=resources.get("Water")-150
            resources["Money"]=resources.get("Money")+200
            for each in resources:
                if resources.get(each) < 0:
                    res+=1
            if res!=0:
                print(f"Sorry, we don't have enough {each} right now,\n you can order something else")
                choice=input("What would you like to have? (latte/espresso/cappuccino): ")
                money = orderplaced()
                sp= pricecal(money)
                change= changecal(sp,money)

            else:
                money = orderplaced()
                sp= pricecal(money)
                change= changecal(sp,money)
        
        case "espresso":
            resources["Coffee"]=resources.get("Coffee")-18
            resources["Milk"]=resources.get("Milk")-0
            resources["Water"]=resources.get("Water")-58
            resources["Money"]=resources.get("Money")+100
            for each in resources:
                if resources.get(each) < 0:
                    res+=1
            if res!=0:
                print(f"Sorry, we don't have enough {each} right now,\n you can order something else")
                choice=input("What would you like to have? (latte/espresso/cappuccino): ")
                money = orderplaced()
                sp= pricecal(money)
                change= changecal(sp,money)

            else:
                money = orderplaced()
                sp= pricecal(money)
                change= changecal(sp,money)


    