weight = float(input("Enter the Weight in Kg : "))
height = float(input("Enter the height in kg : "))

bmi = weight / (height ** 2)

if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<25:
    print("Normal Weight")
else:
    print("Over Weight")
