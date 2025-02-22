import random

#random is a mmodule which we have used

#we can create our own module as well just we will create a seperate py file for it and can import that in the code which you want
print(random.randint(1,10))


print(random.random() * 10)

print(random.uniform(1,10))


input_check = random.randint(0,1)
if input_check == 1:
    print("Tails")
else:
    print("Head")


#List - []

lst_1=[1,2,3]
print(lst_1[0])

#we can get the last value in 2 ways either by positive or by - approach

print(lst_1[2])
print(lst_1[-1])

#List have a lot of functions where you can use for manipulation and creation as well

lst_1.append(4)
print(lst_1)

lst_1.insert(2,5)
print(lst_1)

# say like we have 5 elements in the list and if you are giving list[5] - it will give index out of bound errror

lst_a=[1,2,3]
lst_b=['a','b','b']
lst_all=[lst_a,lst_b]  #Nested List
print(lst_all)
print(lst_all[1][1])

