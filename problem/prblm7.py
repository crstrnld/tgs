def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25.0:
        return "Normal"
    elif 25.0 <= bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
print("BMI Category:", calculate_bmi(weight, height))
