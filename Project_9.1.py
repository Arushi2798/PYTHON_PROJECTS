def changecal(sp,money,choice):
    if sp<0:
        print(f"please give Rs{-sp} more")
        extra=orderplaced()
        money += extra
        new=pricecal(money,choice)
        changecal(new, money,choice)
    elif sp>0 :
        print(f"Here's your change of {sp} rupees")
        print("Enjoy your drink")
    else:
        print("Enjoy your drink")
        
        
def pricecal(money,choice):
    match(choice):
        case "latte":
            sp=money-price.get("latte")
        case "espresso":
            sp=money-price.get("espresso")
        case "cappuccino":
            sp=money-price.get("cappuccino")
    return sp


def orderplaced():
    print("Please insert coins now")
    coin=[5,10,20]
    m=0
    for each in coin:
        coin=int(input(f"How many {each}Rs. coins? : "))
        m+=coin*each
    return m

def resourcecheck():
    res=0
    for each in resources:
        if resources.get(each) < 0:
            res+=1
            break
    if res!=0:
        print(f"Sorry, we don't have enough {each} right now,\n you can order something else")
        
        order()
    else:
        return orderplaced()


def order():
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
            check_money=resourcecheck()
            sp=pricecal(check_money, choice)
            change= changecal(sp,check_money,choice)

        case "cappuccino":
            resources["Coffee"]=resources.get("Coffee")-24
            resources["Milk"]=resources.get("Milk")-100
            resources["Water"]=resources.get("Water")-150
            resources["Money"]=resources.get("Money")+200
            check_money=resourcecheck()
            sp=pricecal(check_money, choice)
            change= changecal(sp,check_money,choice)
            
        case "espresso":
            resources["Coffee"]=resources.get("Coffee")-18
            resources["Milk"]=resources.get("Milk")-0
            resources["Water"]=resources.get("Water")-58
            resources["Money"]=resources.get("Money")+100
            check_money=resourcecheck()
            sp=pricecal(check_money, choice)
            change= changecal(sp,check_money,choice)
            

print("Welcome to the STARBUCKS COFFEE!!")

resources={"Water":500,"Milk":500, "Coffee":50, "Money":0}
price={"latte":150,"espresso":100,"cappuccino":200}

choice=1
while choice:
    order()