import random

print("Welcome to Number Guessing Game!!!")
user_input_1=int(input("Enter your First Number Range: "))
user_input_2=int(input("Enter your Second Number Range: "))
difficulty=input("Choose your Difficulty Level: Type 'easy' or 'Hard' : ").lower()
random_Number=random.randint(user_input_1,user_input_2)
if difficulty=='hard':
    lives_Given=5
elif difficulty=='easy':
    lives_Given=10
else:
    lives_Given=0

def lives_left(lives_Given):
    return lives_Given-1

while lives_Given>0:
    input_Number = int(input(f"Computer has selected a number,choose your number between {user_input_1} and {user_input_2} : "))
    if random_Number == input_Number:
        lives_Given=lives_left(lives_Given)
        print(f"Guessed it correctly, Number is {input_Number}, Total Lives in store: {lives_Given}")
        break
    else:
        lives_Given=lives_left(lives_Given)
        print(f"Guessed Wrongly, Total Lives left in store is {lives_Given}")