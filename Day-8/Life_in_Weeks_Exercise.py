def life_in_Weeks(age,age_max):
    total_age_Left=age_max-age
    return total_age_Left*52

current_year=int(input("What is your current Age : "))
calulate_year=int(input("How many years you want to caluclate for weeks: "))
calc=life_in_Weeks(current_year,calulate_year)
print(f"You have a total of {calc} weeks left")