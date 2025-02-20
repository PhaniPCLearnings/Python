print("Welcome to Python Pizza Deliveries !")
size_Pizza=input("Please Choose the size of Pizza you require : S for Small , M for Medium and L for Large \n")
peperozi=input("Do you require peperozi , Y for Yes and N for No\n")
extra_Cheese=input("Do you Require Extra cheese , Y for Yes and N for No\n")
cost=0
if size_Pizza.lower() == 's':
    cost+=15
elif size_Pizza.lower() =='m':
    cost+=20
elif size_Pizza.lower() == 'l':
    cost+=25
else:
    print("No Data")

if peperozi.lower() =='y':
    cost+=2
else:
    cost=cost

if extra_Cheese.lower()=='y':
    cost+=5
else:
    cost=cost

print(f"Here is the Total amount of your pizza : ${cost}")