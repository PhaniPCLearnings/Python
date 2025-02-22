import random

lst_RPS=['Rock','Paper','Scissors']
computer_choice=random.choice(lst_RPS)
user_choice=input("Select one among the three, Rock, Paper,Scissors.\n")
if user_choice.lower() == 'rock' or user_choice.lower()=='paper' or user_choice.lower()=='scissors':
    print(f"User Selection is {user_choice} and Computer Selection is {computer_choice}")
    if user_choice.lower()==computer_choice.lower():
        print("You Won")
    else:
        print("You Lose")
else:
    print("Invalid Selection")