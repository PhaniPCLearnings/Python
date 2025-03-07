import Coffe_Compositions
print("Welcome to the Coffe Maker Program")
inputType=int(input("Available Choices\n1.Expresso - 100 RS \n2.Latte - 150 RS\n3.Cappucino-125 RS\n Select 1 or 2 or 3: "))
coins_Present=int(input("Please Enter your Amount:"))
if inputType==1:
    Coffe_Compositions.expresso()
    is_Continue=True
elif inputType==2:
    Coffe_Compositions.latte()
    is_Continue = True
elif inputType==3:
    Coffe_Compositions.cappuccino()
    is_Continue = True
else:
    print("Invalid Input")
    is_Continue = False
def Balance_Provided(balance_left):
    if inputType==1:
        return balance_left-100
    elif inputType==2:
        return balance_left-150
    elif inputType==3:
        return balance_left-125
    else:
        return balance_left

while is_Continue==True:
    if inputType==1 and coins_Present>=100:
        print("Enjoy your Expresso :)")
        coins_Present=Balance_Provided(coins_Present)
        continueStill=input(f"Remaining Balance:{coins_Present}, Do you wish to continue,Type y for yes or n for no:").lower()
        if continueStill=='y':
            inputType=int(input("Available Choices\n1.Expresso - 100 RS \n2.Latte - 150 RS\n3.Cappucino-125 RS\n Select 1 or 2 or 3: "))
        else:
            is_Continue=False
    elif inputType==2 and coins_Present>=150:
        print("Enjoy your Latte :)")
        coins_Present=Balance_Provided(coins_Present)
        continueStill=input(f"Remaining Balance:{coins_Present}, Do you wish to continue,Type y for yes or n for no:").lower()
        if continueStill=='y':
            inputType=int(input("Available Choices\n1.Expresso - 100 RS \n2.Latte - 150 RS\n3.Cappucino-125 RS\n Select 1 or 2 or 3: "))
        else:
            is_Continue=False
    elif inputType==3 and coins_Present>=125:
        print("Enjoy your Cappucino :)")
        coins_Present=Balance_Provided(coins_Present)
        continueStill=input(f"Remaining Balance:{coins_Present}, Do you wish to continue,Type y for yes or n for no:").lower()
        if continueStill=='y':
            inputType=int(input("Available Choices\n1.Expresso - 100 RS \n2.Latte - 150 RS\n3.Cappucino-125 RS\n Select 1 or 2 or 3: "))
        else:
            is_Continue=False
    else:
        print("Short of Money!!! Recharge your coins and try again")
        is_Continue=False