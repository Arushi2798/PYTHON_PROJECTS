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

# def resourcecheck(temp):
#     res=0
#     for each in temp:
#         if temp.get(each) < 0:
#             res+=1
#             break
#     if res!=0:
#         print(f"Sorry, we don't have enough {each} right now,\n you can order something else")
#         order()
#     else:
#         return orderplaced()

def program(temp,choice):
    for each in temp:
        if temp.get(each) < 0:
            print(f"Sorry, we don't have enough {each} right now,\n you can order something else")
            break
    else:
        resources["Coffee"]=temp["coffee"]
        resources["Milk"]=temp["milk"]
        resources["Water"]=temp["water"]
        resources["Money"]=temp["paisa"]
        check_money=orderplaced()
        sp=pricecal(check_money, choice)
        changecal(sp,check_money,choice)



def order():
    choice=input("What would you like to have? (latte/espresso/cappuccino): ")
    temp={}
    match choice:
        case "off":
            exit()
        case "report":
            for each in resources:
                print(f"{each} : {resources.get(each)}")

        case "latte":
            temp["coffee"]=resources.get("Coffee")-24
            temp["milk"]=resources.get("Milk")-150
            temp["water"]=resources.get("Water")-200
            temp['paisa']=resources.get("Money")+150
            # check_money=resourcecheck(temp)
            program(temp,choice)

        case "cappuccino":
            resources["Coffee"]=resources.get("Coffee")-24
            resources["Milk"]=resources.get("Milk")-100
            resources["Water"]=resources.get("Water")-150
            resources["Money"]=resources.get("Money")+200
            program(temp)
            
        case "espresso":
            resources["Coffee"]=resources.get("Coffee")-18
            resources["Milk"]=resources.get("Milk")-0
            resources["Water"]=resources.get("Water")-58
            resources["Money"]=resources.get("Money")+100
            program(temp)
        
        case default:
            return "there was a mistake, could you please enter it correctly."
        
    temp.clear()
            

print("Welcome to the STARBUCKS COFFEE!!")

resources={"Water":500,"Milk":500, "Coffee":50, "Money":0}
price={"latte":150,"espresso":100,"cappuccino":200}

choice=1
while choice:
    order()