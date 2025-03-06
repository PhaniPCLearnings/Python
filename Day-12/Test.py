#we can access a variable inside but

enemies=1

def increase_enemies():
    global enemies
    print(f"Defined Enemies{enemies}")
    enemies=2
    print(f"Iniside Function: {enemies}")

increase_enemies()
print(f"Outside Function: {enemies}")


#other way


enemies=1

def increase_enemies():
    return enemies+1

print(f"Before Function: {enemies}")
enemies=increase_enemies()
print(f"Outside Function: {enemies}")
