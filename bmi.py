height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = float(weight / (height ** 2))
rounded = round(bmi)
if bmi <= 18.5:
    print("Your BMI is " + str(rounded))
    print("Underweight")
elif bmi > 18.5 and bmi < 25:
    print("Your BMI is " + str(rounded))
    print("Normal weight")
elif bmi >= 25 and bmi < 30:
    print("Your BMI is " + str(rounded))
    print("Slightly Overweight")
elif bmi >= 30 and bmi < 35:
    print("Your BMI is " + str(rounded))
    print("Overweight")
else:
    print("Your BMI is " + str(rounded))
    print("Obese")
