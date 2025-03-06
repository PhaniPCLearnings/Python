
enemies=1

def increase_enemies():
    print(f"Defined Variable:{enemies}")

increase_enemies()
print(f"Outside Function: {enemies}")

#we can use a global keyword for this but it will not be a best practice

#This will give an error cannot able to access local variable
enemies=1

def increase_enemies():
    print(f"Defined Variable:{enemies}")
    enemies=2
    print(f"Iniside Function: {enemies}")

increase_enemies()
print(f"Outside Function: {enemies}")

#we can use a global keyword for this but it will not be a best practice

enemies=1

def increase_enemies():
    global enemies
    print(f"Defined Enemies{enemies}")
    enemies=2
    print(f"Iniside Function: {enemies}")

increase_enemies()
print(f"Outside Function: {enemies}")