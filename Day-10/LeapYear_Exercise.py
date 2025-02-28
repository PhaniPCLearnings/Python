def is_LeapYear(yearToPass):
    if yearToPass % 4 == 0:
        if yearToPass % 100 == 0:
            if yearToPass % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False



input_year=int(input("Please Enter an Year: "))
is_Lp=is_LeapYear(input_year)
print(is_Lp)