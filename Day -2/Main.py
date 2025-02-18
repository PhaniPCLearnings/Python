#we have lot of data types in python and we have related functions for those data types

#For Example, we have len function when it comes to string but not for integer
#len(12345)

# To overcome this we need to convert the 12345 to string and then check for length

print(len(str(12345)))


#No matter what the value is if it is in "" then we need to refer as string

#We cannot add a integer to a string - Error : Unsupported Operand

#print(123+"456")


# now if we want to check the type of your variable then simply we can go and use keyword type

print(type(12345)) #integer
print(type(12345.123)) #float
print(type("12345"))#string
print(type(True))#boolean


# When you are converting from one datatype to an another be careful with the conversion, this is called Type conversion or Type Casting

#Not all conversions will be there - str to int is highly not possible

print(int("123")+int("456"))

#we can perform multiple operations with python + - * % / and we can perform // which is exclusive for int caluclation but need to be careful

print(5/2) #float result
print(5//2) # int result

#PEMDAS principle to be followed for Caluclations


#we can use ** for power
print(2**3)

print("hello"[0])
print("hello"[4]) # we will get o but we can use negative indexing as well
print("hello"[-1])

