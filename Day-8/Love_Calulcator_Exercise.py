def love_Caluclator(name1,name2):
    total_name=name1+name2
    total_name=total_name.lower()
    t=total_name.count('t')
    r = total_name.count('r')
    u = total_name.count('u')
    e = total_name.count('e')
    l = total_name.count('l')
    o = total_name.count('o')
    v = total_name.count('v')
    e = total_name.count('e')

    first_Digit=t+r+u+e
    second_Digit=l+o+v+e

    return str(first_Digit)+str(second_Digit)

score=love_Caluclator("Angela Yu","Jack Bauer")
print(f"Love Percentage : {score}")
