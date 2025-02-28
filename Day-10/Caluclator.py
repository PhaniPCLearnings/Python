print("Welcome to caluclator Program")


def calc(first_Num,Second_Num,type_Calc):
    if type_Calc=="+":
        return first_Num+Second_Num
    elif type_Calc=='-':
        return first_Num-Second_Num
    elif type_Calc=='*':
        return first_Num*Second_Num
    elif type_Calc=='/':
        return first_Num/Second_Num
    elif type_Calc=='%':
        return first_Num%Second_Num
    else:
        return 'Invalid Input'

to_perform=True

first_Number = int(input("Please Enter your First Number: "))
type_Caluclation = input("What Operation do you need to Perform, '+','-','*','/','%'\n")
second_Number = int(input("Please Enter your Second Number: "))
value_Pres=0
while to_perform:
    value_Pres=calc(first_Number,second_Number,type_Caluclation)
    result=input(f"The result post caluclation is {value_Pres}, Do you want to use it, Y for Yes and N for No: ").lower()
    if result=='y':
        first_Number=value_Pres
        type_Caluclation = input("What Operation do you need to Perform, '+','-','*','/','%'\n")
        second_Number = int(input("Please Enter your another Number: "))
    else:
        first_Number = int(input("Please Enter your First Number: "))
        type_Caluclation = input("What Operation do you need to Perform, '+','-','*','/','%'\n")
        second_Number = int(input("Please Enter your Second Number: "))
    input_choice=input("Do you Still want to continue or close the caluclator, y for continue and n for closing it").lower()
    if input_choice=='y':
        to_perform=True
    else:
        to_perform=False

print(f"Final Count is {value_Pres}")
