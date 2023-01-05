print("Enter your weight in kilogram")
weight = float(input())

print("Enter your height in meter")
height = float(input())

BMI = weight / ( height * height )

print("BMI = ",round(BMI,2),"kg/m²")

if BMI >= 40 :
    print("Calss III obesity")

elif BMI >= 35 and BMI < 40 :
    print("Class II obesity")

elif BMI >= 30 and BMI < 35 :
    print("Class II obesity")

elif BMI >= 25 and BMI < 30 :
    print("Overweight")

elif BMI >=18.5 and BMI < 25 :
    print("Optium range")

elif BMI < 18.5 :
    print("Underweight")

else:
    print("Please change your values")
