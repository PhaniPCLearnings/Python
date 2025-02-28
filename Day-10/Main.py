def func_TitleCase(f_name,l_name):
    Full_Name=f_name.title()+" "+l_name.title()
    print("Hello MR. "+Full_Name)

func_TitleCase("PhAni","chErrY")

#we can use return keyword as well to get the results

#Advantage of return keyword is we can use it as an input to an another function

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2


"""
This is called docstring where we can write multiple lines of code
We are adding up two numbers and result of it will be used for subtraction
once the substraction has been done it will print the results
"""

num=add(11,9)
subtr=sub(num,10)
print(subtr)


def innerfunc(a,b):
    def outerfunc(c,d):
        return c+d
    return outerfunc(a,b)

ab=innerfunc(5,10)
print(ab)


def fnc(a):
    if a<40:
        return
        print("Terrible")
    elif a<80:
        return "Pass"
    else:
        return "True"

ac=fnc(25)
print(ac)