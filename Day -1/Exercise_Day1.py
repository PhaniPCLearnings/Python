print("Hey Sir/Madam Welcome to Band Name Generator Program")

name_City=input("Please Enter the Name of the city you grew up in?\n")
pet_Name=input("Please Enter your Petname?\n")
name_Start=input("Please Enter how you want to Name your Band.\nPress P if you want to start with your petname\npress n if you want to start with your city\n")
if name_Start.lower()=="p":
    Band_Name=pet_Name+" "+name_City
    print()
elif name_Start.lower()=="n":
    Band_Name=name_City+" "+pet_Name
else:
    Band_Name="Sorry, You have entered a wrong Input!!! Unable to create a Band Name for you, Please try Again"

print(Band_Name)