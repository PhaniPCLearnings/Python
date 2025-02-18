print("Welcome to the Tip Caluclator Program")
total_Bill=float(input("Please Enter the Total Bill Amount in $ : "))
tip_Given=int(input("How Much Tip would you like to give ? 10,12,15 or any other percent: "))
people_Available=int(input("How many people want to split the bill: "))

tip_Caluclator = total_Bill+(total_Bill*float(tip_Given)/100)
each_Person_Bill=round(tip_Caluclator/people_Available,2)
print(each_Person_Bill)
print(f"Each Person has to pay an amount of $ {each_Person_Bill}")