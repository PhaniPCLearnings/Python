import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards=[random.choice(cards),random.choice(cards)]
computer_cards=[random.choice(cards),random.choice(cards)]
print(user_cards)
print(computer_cards)

def cards_pick(cardsPicked):
    return sum(cardsPicked)

user_sum=cards_pick(user_cards)
print(user_sum)
computer_sum=cards_pick(computer_cards)
print(computer_sum)

if user_sum==21:
    print("User Has got a Black Jack, User Won")
elif computer_sum==21:
    print("Computer has got a black jack,Computer Won")
else:
    if user_sum>21:
        if 11 in user_cards:
            user_cards[user_cards.index(11)]=1
            new_us=cards_pick(user_cards)
            print(new_us)
        else:
            pass
    elif computer_sum>21:
        if 11 in computer_cards:
            computer_cards[computer_cards.index(11)]=1
            new_cs=cards_pick(computer_cards)
            print(new_cs)
        else:
            pass
    elif user_sum>16:
        input_user=input("Do you want to pick an another card: Y for Yes and N for No: ").lower()
        if input_user=="y":
            user_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))
            sum_user=cards_pick(user_cards)
            sum_Cmp=cards_pick(computer_cards)
        else:
            sum_user=user_sum
            sum_Cmp=computer_sum
        if sum_user>sum_Cmp:
            print(f"User Has Won, User Points:{sum_user},Computer Points: {sum_Cmp}")
        elif sum_user<sum_Cmp:
            print("Computer Has won, User Points:{sum_user},Computer Points: {sum_Cmp}")
        else:
            print("Draw Match")
    else:
        sum_user=cards_pick(user_cards)
        sum_Cmp=cards_pick(computer_cards)
        print(sum_Cmp)
        print(sum_user)
        if sum_user>sum_Cmp:
            print(f"User Has Won, User Points:{sum_user},Computer Points: {sum_Cmp}")
        elif sum_user<sum_Cmp:
            print("Computer Has won, User Points:{sum_user},Computer Points: {sum_Cmp}")
        else:
            print("Draw Match")
