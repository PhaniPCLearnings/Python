import string

print("Hello World!")
print("Hello World!")
print("Hello World!")


# same code can be written in below

print(3 * "Hello World!\n")

#Combine Different Strings

print("Hello"+" "+"Phani")

# If we have unnecessary spaces then it will lead to intendation Error - Be careful with space in Python

# If we are giving something wrong then it will lead to syntax error

#If we have a variable and we have given name wrongly somewhere in the code it will lead to NameError

# we have input function which take input from user and perform the operations

Name_User=input("What is Your Name? : ")
Age_User=int(input("Please Enter your Age : "))

print("My Name is "+Name_User+" and I'm "+str(Age_User))

#Another Way of Writting is it By means of Fstring

print(f"My Name is {Name_User} and I'm {Age_User}")

#Make sure that your code is readable

#we can have multiple words but dont keep space we can use _ if we use space there are complications involved

#We can use Numbers but dont start at the begining

#Dont use name of a function

