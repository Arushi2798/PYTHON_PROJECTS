#Question Statement
"""Creating a CALCULATOR"""

from os import system

def calculation(num1,num2,op):
    if op=="+":
        return num1+num2
    if op=="-":
        return num1-num2   
    if op=="*":
            return num1*num2    
    if op=="/":
            return num1/num2    
    

# num_1=int(input("Enter your 1st number: "))
# print("Operand List: \n+\n-\n*\n/")
# cal=input("Select an operand from the list above: ")
# num_2=int(input("Enter your next number: "))

# res=calculation(num_1,num_2,cal)
# print(res)

choice="n"
while choice:  
    if choice=="n":
        num_1=int(input("Enter your 1st number: "))
        print("Operand List: \n+\n-\n*\n/")
        cal=input("Select an operand from the list given above: ")
        num_2=int(input("Enter your next number: "))

        res=calculation(num_1,num_2,cal)
        print(f'{num_1}{cal}{num_2}={res}')
        choice=input(f"Enter 'y' to continue calculation with {res} or 'n' to start new calculation or 'x' to exit: ")

    elif choice=='y':
        num_1=res
        cal=input("Select an operand from the list given above: ")
        num_2=int(input("Enter your next number: "))
        res=calculation(num_1,num_2,cal)
        print(res)
        
        choice=input(f"Enter 'y' to continue calculation with {res} or 'n' to start new calculation or 'x' to exit: ")
    elif choice=='x':
        print("exit calculator")
        break
    else:
        print("something is wrong with your input")
        break
