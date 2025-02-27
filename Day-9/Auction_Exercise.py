print("Welcome to the Secret Auction Program")
dict_SecretAuction={}
first_name=input("Please Enter your Name : ")
first_Amount=int(input("Please Enter your Amount: "))
dict_SecretAuction[first_name]=first_Amount
input_Auction=input("Do the Auction Still continue : Yes or No : \n").lower()
while input_Auction=='yes':
    name_Person=input("Please Enter your Name : ")
    amount_Person=int(input("Please Enter your Amount: "))
    dict_SecretAuction[name_Person]=amount_Person
    input_Auction=input("Do the Auction Still continue : Yes or No : \n").lower()


def highest_Bidder(bidding_dictionary):
    highest_Bid=0
    for i in bidding_dictionary.keys():
        if highest_Bid<bidding_dictionary[i]:
            highest_Bid=bidding_dictionary[i]
            highest_key=i
        else:
            highest_Bid=highest_Bid
    return highest_Bid,highest_key


check_highest=highest_Bidder(dict_SecretAuction)
print(f"The Highest Bid is {check_highest[0]} and Person won is {check_highest[1]}")


#another Way
print(max(dict_SecretAuction,key=dict_SecretAuction.get))

